#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud, ChannelFloat32

if __name__ == '__main__':
    rospy.init_node('point_cloud_publisher')

    cloud_pub = rospy.Publisher('cloud', PointCloud, queue_size=50)

    num_points = 100
    count = 0
    rate = rospy.Rate(1.0)

    while not rospy.is_shutdown():
        cloud = PointCloud()
        cloud.header.stamp = rospy.Time.now()
        cloud.header.frame_id = "sensor_frame"

        cloud.points = [None] * num_points
        cloud.channels = [ChannelFloat32()] * 1
        cloud.channels[0].name = "intensities"
        cloud.channels[0].values = [0] * num_points

        # generate some fake data for our point cloud
        for i in range(num_points):
            cloud.points[i].x = 1 + count
            cloud.points[i].y = 2 + count
            cloud.points[i].z = 3 + count
            cloud.channels[0].values[i] = 100 + count

        cloud_pub.publish(cloud)
        count += 1
        rate.sleep()
