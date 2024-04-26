#!/usr/bin/env python3
import rospy
from nav_msgs.msg import OccupancyGrid
from nav_msgs.srv import GetMap

from map_maker import AddObject, add_object, create_occupancymap, create_costmap
from interfaces.srv import AddObjectSrv
import yaml
import os
import numpy as np


def read_pgm(pgmf):
    """Return a raster of integers from a PGM as a list of lists."""
    assert pgmf.readline() == b'P5\n'
    (width, height) = [int(i) for i in pgmf.readline().split()]
    depth = int(pgmf.readline())
    assert depth <= 255

    raster = []
    for _ in range(height * width):
        # 0 => Free, 33 => Unknown, 85 => Occupied
        value = int.from_bytes(pgmf.read(1), 'big') // 3
        raster.append(value)
    return width, height, raster



class MapServer:
    def __init__(self):
        rospy.init_node('map_node', anonymous=True)

        self.map = None
        self.costmap = None

        self.object_map = None
        self.objects = []

        self.yaml_filename = rospy.get_param('/yaml_filename', '')
        self.frame_id = rospy.get_param('~frame_id', 'map')
        self.inflation = rospy.get_param('~inflation', 10)

        self.add_object_service = rospy.Service('add_object', AddObjectSrv, self.add_object_callback)
        self.occ_service = rospy.Service('get_map', GetMap, self.get_map_callback)
        self.occ_pub = rospy.Publisher('map', OccupancyGrid, queue_size=1, latch=True)
        self.costmap_pub = rospy.Publisher('costmap', OccupancyGrid, queue_size=1, latch=True)

        self.on_configure(None)
    
    def add_object_callback(self, request: AddObject):
        self.objects.append(request)
        self.object_map = add_object(self.object_map, request)
        self.map.data = create_occupancymap(self.object_map)
        self.costmap.data = create_costmap(self.object_map, self.inflation)
        
        self.occ_pub.publish(self.map)
        self.costmap_pub.publish(self.costmap)

        rospy.loginfo('Updated costmap and occupancy map')
        return True

    def get_map_callback(self, request):
        if self.map:
            return self.map
        return None

    def on_configure(self, state):
        rospy.loginfo('Configuring')

        if self.yaml_filename:
            if not self.load_map_from_yaml(self.yaml_filename):
                raise RuntimeError("Failed to load map yaml file: " + self.yaml_filename)
        else:
            rospy.logerr("yaml-filename parameter is empty")
        
        self.occ_pub.publish(self.map)
        self.costmap_pub.publish(self.costmap)

    def on_cleanup(self, state):
        self.occ_pub.destroy()
        self.add_object_service.destroy()
        self.occ_service.destroy()
        self.object_map = None
        self.objects = []
        self.map = None
    
    def load_map_from_yaml(self, yaml_file):
        with open(yaml_file, 'r') as file:
            yaml_data = yaml.safe_load(file)

        yaml_dir = os.path.dirname(yaml_file)
        image_path = os.path.join(yaml_dir, yaml_data['image'])
        objectmap_path = os.path.join(yaml_dir, yaml_data['objectmap'])

        width, height, image = read_pgm(open(image_path, 'rb'))
        resolution = yaml_data['resolution']
        origin = yaml_data['origin']
        object_map = np.loadtxt(objectmap_path)

        # Create Object Map
        self.object_map = object_map
        self.objects = []

        # Load Occupancy Map
        map = OccupancyGrid()
        map.header.frame_id = self.frame_id
        map.info.width = width
        map.info.height = height
        map.info.resolution = resolution
        map.info.origin.position.x = origin[0]
        map.info.origin.position.y = origin[1]
        map.info.origin.position.z = origin[2]
        map.info.origin.orientation.x = 0.0 #origin[3]
        map.info.origin.orientation.y = 0.0 #origin[4]
        map.info.origin.orientation.z = 0.0 #origin[5]
        map.info.origin.orientation.w = 0.0 #origin[6]
        map.data = create_occupancymap(object_map)
        self.map = map

        self.costmap = OccupancyGrid()
        self.costmap.header.frame_id = self.frame_id
        self.costmap.info = map.info
        self.costmap.data = create_costmap(object_map, self.inflation)
        
        rospy.loginfo("Loaded yaml file!")
        rospy.loginfo((min(image), max(image)))
        return True

def main(args=None):
    try:
        mapserver = MapServer()
        rospy.spin()
    except rospy.ROSException:
        pass

if __name__ == '__main__':
    main()

