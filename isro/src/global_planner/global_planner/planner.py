import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid, Path


class CustomPlannerNode(Node):
    def __init__(self):
        super().__init__('custom_planner_node')
        self.goal_pose_subscription = self.create_subscription(
            PoseStamped,
            '/move_base/goal',
            self.goal_pose_callback,
            10)
        self.map_subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10)
        

        self.path_pub = self.create_publisher(Path, '/path', 1)
        self.map = None
        self.robot_footprint = None

    def goal_pose_callback(self, msg: PoseStamped):
        # Implement your custom planning logic here:
        # 1. Receive the goal pose from the message.
        # 2. Utilize a planning algorithm (e.g., Dijkstras, A*) or other approach.
        # 3. Generate a collision-free path based on your map and robot constraints.
        # 4. Optionally, publish the planned path for visualization.
        if not self.map:
            self.get_logger().warn('No map available')
            return

        goal_pose = msg.pose
        planned_path = self.astar_planning(self.map, self.robot_footprint, goal_pose)

        if planned_path is not None:
            path_msg = Path()
            for pose in planned_path:
                path_msg.poses.append(PoseStamped(pose=pose))
            # Publish the path message (replace with your publisher setup)
            self.path_pub.publish(path_msg)
            self.get_logger().info("Planned path published!")
        else:
            # Planning failed, handle appropriately (e.g., log message)
            self.get_logger().warn("Path planning failed!")

    def map_callback(self, msg: OccupancyGrid):
        self.map = msg.data
        self.get_logger().info('Map Received')

# Main function to run the node
def main():
    rclpy.init()
    node = CustomPlannerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
