#!/usr/bin/env python3
import numpy as np
import rospy
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped

from AStarPlanner import AStarPlanner

algorithms = {
    'AStarPlanner': AStarPlanner
}

class GlobalPlanner:
    def __init__(self):
        super().__init__()
        rospy.init_node('global_planner')

        self.frame_id = rospy.get_param('~frame_id', 'map')
        self.algorithm_name = rospy.get_param('~algorithm', 'AStarPlanner')

        self.costmap = None
        self.initial_pose = None
        self.goal_pose = None
        self.algorithm = None

        self.initial_pose_sub = rospy.Subscriber('/initialpose', PoseWithCovarianceStamped, self.set_initial_pose)
        self.goal_pose_sub = rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.set_goal_pose)
        self.costmap_sub = rospy.Subscriber('/costmap', OccupancyGrid, self.update_costmap)
        self.plan_pub = rospy.Publisher('plan', Path, queue_size=1, latch=True)
        self.on_configure()

    def on_configure(self):
        self.algorithm = algorithms[self.algorithm_name]()
        rospy.loginfo("Configured global planner")

    def update_costmap(self, costmap: OccupancyGrid):
        height = costmap.info.height
        width = costmap.info.width
        self.costmap = np.array(costmap.data, dtype='int8').reshape((height, width))
        rospy.loginfo(f"Received costmap")
    
    def set_initial_pose(self, start: PoseWithCovarianceStamped):
        self.initial_pose = start.pose
        rospy.loginfo(f"Received initial pose")

    def set_goal_pose(self, goal: PoseStamped):
        self.goal_pose = goal
        rospy.loginfo(f"Received goal pose")

        self.make_plan()

    def make_plan(self):
        if self.costmap is None or self.initial_pose == None or self.goal_pose == None:
            return rospy.logwarn("No costmap or initial pose set")
        
        costmap = self.costmap
        start = (int(self.initial_pose.pose.position.y * 100), int(self.initial_pose.pose.position.x * 100))
        goal = (int(self.goal_pose.pose.position.y * 100), int(self.goal_pose.pose.position.x * 100))

        print(start, goal)
        path = self.algorithm.search(costmap, start, goal)
        if not path:
            rospy.logwarn('Could not find path to goal')
            return

        plan = Path()
        plan.header.frame_id = self.frame_id
        plan.poses = [self.point_to_posestamped(x) for x in path]

        self.plan_pub.publish(plan)
        rospy.loginfo("Published path")

    def point_to_posestamped(self, point):
        pose = PoseStamped()
        pose.header.frame_id = self.frame_id
        pose.pose.position.x = point[1] / 100
        pose.pose.position.y = point[0] / 100
        return pose


def main(args=None):
    try:
        planner = GlobalPlanner()
        rospy.spin()
    except rospy.ROSException:
        pass


if __name__ == '__main__':
    main()
