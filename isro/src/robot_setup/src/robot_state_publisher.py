#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import TransformStamped
from tf.transformations import quaternion_from_euler

if __name__ == '__main__':
    rospy.init_node('robot_tf_publisher')

    rate = rospy.Rate(100)

    broadcaster = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        quaternion = quaternion_from_euler(0, 0, 0)
        translation = (0.1, 0.0, 0.2)
        broadcaster.sendTransform(
            translation,
            quaternion,
            rospy.Time.now(),
            "base_camera",
            "base_link"
        )
        rate.sleep()
