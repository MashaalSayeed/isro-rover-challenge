#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from nav_msgs.srv import GetMap

from map_server_node.map_maker import AddObject, add_object, make_costmap
from interfaces.srv import AddObjectSrv

import yaml
import os
import numpy as np

# yaml file
# height:
# width :
 
def read_pgm(pgmf):
    """Return a raster of integers from a PGM as a list of lists."""
    # print(pgmf.readline())
    assert pgmf.readline() == b'P5\n'
    (width, height) = [int(i) for i in pgmf.readline().split()]
    depth = int(pgmf.readline())
    assert depth <= 255

    raster = []
    for y in range(height):
        for y in range(width):
            raster.append(int.from_bytes(pgmf.read(1), 'big') // 3)
    return width, height, raster


class MapServer(Node):
    def __init__(self):
        super().__init__('map_server')

        self.map = OccupancyGrid()
        self.object_map = None
        self.objects = []

        self.yaml_filename = self.declare_parameter('yaml_filename', '').get_parameter_value().string_value
        self.frame_id = self.declare_parameter('frame_id', 'map').get_parameter_value().string_value

        self.add_object_service = self.create_service(AddObjectSrv, 'add_object', self.add_object_callback)
        self.occ_service = self.create_service(GetMap, 'get_map', self.get_map_callback)
        self.occ_pub = self.create_publisher(OccupancyGrid, 'map', 1)

        self.on_configure(None)
    
    def add_object_callback(self, request, response):
        obj = AddObject
        obj.tag = request.tag
        obj.pose = request.pose

        self.objects.append(obj)
        self.object_map = add_object(self.object_map, obj)
        self.get_logger().debug(self.object_map.shape)
        self.map.data = make_costmap(self.object_map)
        self.occ_pub.publish(self.map)

        response.success = True
        return response

    def get_map_callback(self, request, response):
        if self.map:
            response.map = self.map
        return response

    def on_configure(self, state):
        self.get_logger().info('Configuring')

        if self.yaml_filename:
            if not self.load_map_from_yaml(self.yaml_filename):
                raise RuntimeError("Failed to load map yaml file: " + self.yaml_filename)
        else:
            self.get_logger().info("yaml-filename parameter is empty")

    def on_activate(self, state):
        if self.map:
            self.occ_pub.publish(self.map)
        self.get_logger().info('Activating Node')

    def on_deactivate(self, state):
        self.get_logger().info('Deactivating')

    def on_cleanup(self, state):
        self.occ_pub.destroy()
        self.add_object_service.destroy()
        self.occ_service.destroy()
        self.object_map = None
        self.objects = []
        self.map = OccupancyGrid()

    def on_shutdown(self, state):
        pass

    def load_map_from_yaml(self, yaml_file):
        with open(yaml_file, 'r') as file:
            yaml_data = yaml.safe_load(file)

        image_path = os.path.join(os.path.dirname(yaml_file), yaml_data['image'])
        width, height, image = read_pgm(open(image_path, 'rb'))
        # width = yaml_data['image']['width']
        # height = yaml_data['image']['height']
        resolution = yaml_data['resolution']
        origin = yaml_data['origin']

        # Load Map
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
        map.data = image#[0] * (width * height)

        self.object_map = np.zeros((width, height))
        self.objects = []
        self.map = map
        self.occ_pub.publish(self.map)
        
        self.get_logger().info("Loaded yaml file!")
        return True

def main(args=None):
    rclpy.init(args=args)
    node = MapServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

