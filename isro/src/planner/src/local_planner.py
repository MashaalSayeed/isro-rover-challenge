#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Twist
from TEBLocalPlanner import TEBLocalPlanner
from DWALocalPlanner import DWALocalPlanner

import math


algorithms = {
    'TEBLocalPlanner': TEBLocalPlanner,
    'DWALocalPlanner': DWALocalPlanner
}

class LocalPlanner:
    def __init__(self):
        self.__init__()
        rospy.init_node('local_planner')

        self.frame_id = rospy.get_param('~frame_id', 'map')
        self.algorithm_name = rospy.get_param('~algorithm', 'DWALocalPlanner')

        self.global_plan = None
        self.odom = None

        self.plan_sub = rospy.Subscriber('/plan', Odometry, self.plan_callback)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odometry_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.on_configure()

    def on_configure(self):
        self.algorithm = algorithms[self.algorithm_name]()
        rospy.loginfo("Configured local planner")

    def plan_callback(self, plan: Path):
        self.global_plan = plan

    def odometry_callback(self, odom: Odometry):
        self.odom = odom

    def compute_velocity_commands(self):
        target_pose = self.global_plan[0]
        robot_pose = self.odom.pose.pose
        v_linear = 1.0
        theta = robot_pose.orientation.w
        dx = target_pose.pose.position.x - robot_pose.position.x
        dy = target_pose.pose.position.y - robot_pose.position.y

        desired_theta = math.atan2(dy, dx)
        omega = v_linear * (desired_theta - theta) / self.robot_radius

        cmd_vel = {'linear': v_linear, 'angular': omega}
        return cmd_vel



def main(args=None):
    try:
        planner = LocalPlanner()
        rospy.spin()
    except rospy.ROSException:
        pass
