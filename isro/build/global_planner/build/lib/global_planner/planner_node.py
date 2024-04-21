import rclpy
from rclpy.action import SimpleActionServer
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from lifecycle_msgs.msg import State
from nav2_msgs.action import ComputePathToPose, ComputePathThroughPoses
from nav2_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from rclpy.qos import QoSProfile
from rclpy.time import Time
from tf2_ros import TransformBroadcaster, TransformListener
from threading import Thread

class PlannerServer(Node):

    def __init__(self, options):
        super().__init__("planner_server", options)
        self.get_logger().info("Creating")

        self.declare_parameter("expected_planner_frequency", 1.0)
        self.declare_parameter("action_server_result_timeout", 10.0)

        self.planner_ids = self.get_parameter("planner_plugins").as_str_list()
        # self.default_ids = ["GridBased"]
        # self.default_types = ["nav2_navfn_planner.NavfnPlanner"]
        self.costmap_ = None

        # Setup the global costmap
        # self.costmap_ros_ = PyCostmap2D(
        #     "global_costmap", self.get_namespace(), "global_costmap",
        #     self.get_parameter("use_sim_time").as_bool())

        # # Launch a thread to run the costmap node
        # self.costmap_thread = Thread(target=self.costmap_ros_.run)
        # self.costmap_thread.start()

        self.tf_ = TransformListener(self)
        self.tf_broadcaster = TransformBroadcaster(self)

        self.planners_ = {}
        self.planner_types_ = []

        # for i in range(len(self.planner_ids)):
        #     try:
        #         self.planner_types_.append(get_plugin_type_param(self, self.planner_ids[i]))
        #         planner = GlobalPlanner.create_instance(self.planner_types_[i])
        #         self.get_logger().info(f"Created global planner plugin {self.planner_ids[i]} of type {self.planner_types_[i]}")
        #         planner.configure(self, self.planner_ids[i], self.tf_, self.costmap_ros_)
        #         self.planners_[self.planner_ids[i]] = planner
        #     except Exception as ex:
        #         self.get_logger().fatal(f"Failed to create global planner. Exception: {ex}")
        #         rclpy.shutdown()

        self.planner_ids_concat = " ".join(self.planner_ids)
        self.get_logger().info(f"Planner Server has {self.planner_ids_concat} planners available.")

        self.expected_planner_frequency = float(self.get_parameter("expected_planner_frequency").as_double())
        if self.expected_planner_frequency > 0:
            self.max_planner_duration = 1 / self.expected_planner_frequency
        else:
            self.get_logger().warn("The expected planner frequency parameter is negative. It should be greater than 0.0 to turn on duration overrun warning messages")
            self.max_planner_duration = 0.0

        # Initialize publishers & subscribers
        self.plan_publisher = self.create_publisher(Path, "plan", 1)

        self.action_server_poses_ = SimpleActionServer(
            ComputePathThroughPoses,
            self,
            "compute_path_through_poses",
            execute_callback=self.compute_plan_through_poses,
            qos_profile=QoSProfile(depth=10, keep_last=1))

        # self.on_set_parameters_callback = on_set_parameters_callback(self)
        # self.set_parameter_callback(self.on_set_parameters_callback)

        self.timeout = Time(seconds=float(self.get_parameter("action_server_result_timeout").as_double()))

    def destroy(self):
        self.costmap_ros_.shutdown()
        self.costmap_thread.join()
        super().destroy()

    def compute_plan(self, goal_pose):
        start_time = self.get_clock().now()

        plan = Path()
        selected_planner = None

        # Choose a planner based on user configuration (priority?)
        for planner_id, planner in self.planners_.items():
            selected_planner = planner
            break

        if selected_planner is None:
            self.get_logger().warn("No planner available")
            return #CallbackReturn.FAILURE

        result = selected_planner.compute_path(goal_pose)

        # if result != FootprintCollisionChecker.SUCCESS:
        #     self.get_logger().info(f"Planner {selected_planner.planner_id_} failed to compute a path.")
        #     return #CallbackReturn.FAILURE

        plan.poses = selected_planner.get_path()
        self.plan_publisher.publish(plan)

        duration = self.get_clock().now() - start_time
        if duration > self.max_planner_duration:
            self.get_logger().warn(f"Planner '{selected_planner.planner_id_}' took too long: {duration.nanoseconds / 1e9:.2f} seconds. Expected planner frequency is {self.expected_planner_frequency:.2f} Hz.")

        return #CallbackReturn.SUCCESS

    def compute_plan_through_poses(self, goal_poses):
        start_time = self.get_clock().now()

        plan = Path()
        selected_planner = None

        # Choose a planner based on user configuration (priority?)
        for planner_id, planner in self.planners_.items():
            selected_planner = planner
            break

        if selected_planner is None:
            self.get_logger().warn("No planner available")
            return #CallbackReturn.FAILURE

        result = selected_planner.compute_path_through_poses(goal_poses)

        # if result != FootprintCollisionChecker.SUCCESS:
        #     self.get_logger().info(f"Planner {selected_planner.planner_id_} failed to compute a path.")
        #     return CallbackReturn.FAILURE

        plan.poses = selected_planner.get_path()
        self.plan_publisher.publish(plan)

        duration = self.get_clock().now() - start_time
        if duration > self.max_planner_duration:
            self.get_logger().warn(f"Planner '{selected_planner.planner_id_}' took too long: {duration.nanoseconds / 1e9:.2f} seconds. Expected planner frequency is {self.expected_planner_frequency:.2f} Hz.")

        return #CallbackReturn.SUCCESS

def main(arguments=None):
    rclpy.init(arguments=arguments)

    options = rclpy.NodeOptions()
    options.auto_declare = True

    planner_server = PlannerServer(options)

    # Interrupt handler to detect ROS shutdown
    def shutdown_handler():
        planner_server.destroy()
        rclpy.shutdown()

    rclpy.spin(planner_server, shutdown_signal=shutdown_handler)

    rclpy.shutdown()


if __name__ == "__main__":
    main()

