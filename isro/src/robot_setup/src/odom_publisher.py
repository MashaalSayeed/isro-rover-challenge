#!/usr/bin/env python

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Pose, Twist, Vector3
import math


if __name__ == '__main__':
    rospy.init_node('odometry_publisher')

    odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)
    odom_broadcaster = tf.TransformBroadcaster()

    x = 0.0
    y = 0.0
    th = 0.0

    vx = 0.1
    vy = -0.1
    vth = 0.1

    current_time = rospy.Time.now()
    last_time = rospy.Time.now()

    rate = rospy.Rate(3.0)

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        dt = (current_time - last_time).to_sec()
        delta_x = (vx * math.cos(th) - vy * math.sin(th)) * dt
        delta_y = (vx * math.sin(th) + vy * math.cos(th)) * dt
        delta_th = vth * dt

        x += delta_x
        y += delta_y
        th += delta_th

        odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

        # Publish the transform over tf
        odom_broadcaster.sendTransform(
            (x, y, 0.),
            odom_quat,
            current_time,
            "base_link",
            "odom"
        )

        # Publish the odometry message over ROS
        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"

        # Set the position
        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

        # Set the velocity
        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

        odom_pub.publish(odom)

        last_time = current_time
        rate.sleep()
