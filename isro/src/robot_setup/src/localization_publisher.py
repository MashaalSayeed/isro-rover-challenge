#!/usr/bin/env python

import rospy

from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage

def main():
  rospy.init_node('dummy_tf_publisher')

  # Set desired transform values (adjust these as needed)
  x = 2.0
  y = 1.5
  z = 0
  roll = 0.0  # Radians
  pitch = 0.0  # Radians
  yaw = 0.0  # Radians

  # Define a function to create a TF message
  def create_tf_message(translation, rotation):
    tf_msg = TFMessage()
    transform = TransformStamped()
    transform.header.stamp = rospy.Time.now()
    transform.header.frame_id = "map"
    transform.child_frame_id = "odom"

    transform.transform.translation.x = translation[0]
    transform.transform.translation.y = translation[1]
    transform.transform.translation.z = translation[2]

    # Define rotation using quaternion (represents no rotation initially)
    transform.transform.rotation.w = rotation[0]
    transform.transform.rotation.x = rotation[1]
    transform.transform.rotation.y = rotation[2]
    transform.transform.rotation.z = rotation[3]

    tf_msg.transforms.append(transform)
    return tf_msg

  # Create a publisher for TF messages
  pub = rospy.Publisher('/tf', TFMessage, queue_size=10)

  rate = rospy.Rate(10)  # 10 Hz publishing rate

  while not rospy.is_shutdown():
    # Define translation and rotation as lists
    translation = [x, y, z]
    rotation = [1.0, 0.0, 0.0, 0.0]  # Quaternion for no rotation

    # Create and publish the TF message
    tf_msg = create_tf_message(translation, rotation)
    pub.publish(tf_msg)
    # rospy.spinOnce()
    rate.sleep()

if __name__ == '__main__':
  main()