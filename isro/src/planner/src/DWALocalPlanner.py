import math
import rospy

from collections import namedtuple
from dataclasses import dataclass

State = namedtuple('State', ['x', 'y', 'theta', 'velocity', 'yawrate'])
Cost = namedtuple('Cost', ['to_goal_cost', 'obs_cost', 'speed_cost', 'path_cost', 'total_cost'])
Window = namedtuple('Window', ['min_velocity', 'max_velocity', 'min_yawrate', 'max_yawrate'])




class DWALocalPlanner:
    def __init__(self):
        self.target_velocity = rospy.get_param('~TARGET_VELOCITY', 0.55)
        self.max_velocity = rospy.get_param('~MAX_VELOCITY', 1.0)
        self.min_velocity = rospy.get_param('~MIN_VELOCITY', 0.0)
        self.max_yawrate = rospy.get_param('~MAX_YAWRATE', 1.0)
        self.min_yawrate = rospy.get_param('~MIN_YAWRATE', 0.05)
        self.max_in_place_yawrate = rospy.get_param('~MAX_IN_PLACE_YAWRATE', 0.6)
        self.min_in_place_yawrate = rospy.get_param('~MIN_IN_PLACE_YAWRATE', 0.3)
        self.max_acceleration = rospy.get_param('~MAX_ACCELERATION', 0.5)
        self.max_deceleration = rospy.get_param('~MAX_DECELERATION', 1.0)
        self.max_d_yawrate = rospy.get_param('~MAX_D_YAWRATE', 3.2)
        self.angle_resolution = rospy.get_param('~ANGLE_RESOLUTION', 0.087)
        self.predict_time = rospy.get_param('~PREDICT_TIME', 3.0)
        self.dt = rospy.get_param('~DT', 0.1)
        self.sleep_time_after_finish = rospy.get_param('~SLEEP_TIME_AFTER_FINISH', 0.5)
        self.obs_cost_gain = rospy.get_param('~OBSTACLE_COST_GAIN', 1.0)
        self.to_goal_cost_gain = rospy.get_param('~TO_GOAL_COST_GAIN', 1.0)
        self.speed_cost_gain = rospy.get_param('~SPEED_COST_GAIN', 0.1)
        self.path_cost_gain = rospy.get_param('~PATH_COST_GAIN', 0.0)
        self.dist_to_goal_th = rospy.get_param('~GOAL_THRESHOLD', 0.3)
        self.turn_direction_th = rospy.get_param('~TURN_DIRECTION_THRESHOLD', 1.0)
        self.angle_to_goal_th = rospy.get_param('~ANGLE_TO_GOAL_TH', math.pi)
        self.sim_direction = rospy.get_param('~SIM_DIRECTION', math.pi / 2.0)
        self.slow_velocity_th = rospy.get_param('~SLOW_VELOCITY_TH', 0.1)
        self.obs_range = rospy.get_param('~OBS_RANGE', 2.5)
        self.use_footprint = rospy.get_param('~USE_FOOTPRINT', False)
        self.use_path_cost = rospy.get_param('~USE_PATH_COST', False)
        self.subscribe_count_th = rospy.get_param('~SUBSCRIBE_COUNT_TH', 3)
        self.velocity_samples = rospy.get_param('~VELOCITY_SAMPLES', 3)
        self.yawrate_samples = rospy.get_param('~YAWRATE_SAMPLES', 20)

    def dwa_planning(self, goal, trajectories):
        min_cost = Cost(0.0, 0.0, 0.0, 0.0, float('inf'))
        dynamic_window = self.calculate_dynamic_window()
        trajectory_size = int(self.predict_time / self.dt)
        best_traj = [State(0.0, 0.0, 0.0, 0.0, 0.0)] * trajectory_size
        costs: list[Cost] = []
        velocity_resolution = max((dynamic_window.max_velocity - dynamic_window.min_velocity) / (self.velocity_samples - 1), 1e-9)
        yawrate_resolution = max((dynamic_window.max_yawrate - dynamic_window.min_yawrate) / (self.yawrate_samples - 1), 1e-9)

        available_traj_count = 0
        for i in range(self.velocity_samples):
            v = dynamic_window.min_velocity + velocity_resolution * i
            for j in range(self.yawrate_samples):
                y = dynamic_window.min_yawrate + yawrate_resolution * j
                if v < self.slow_velocity_th:
                    y = max(y, self.min_yawrate) if y > 0 else min(y, -self.min_yawrate)
                traj = self.generate_trajectory(v, y)
                cost = self.evaluate_trajectory(traj, goal)
                costs.append(cost)
                if cost.obs_cost == float('inf'):
                    traj_available = False
                else:
                    traj_available = True
                    available_traj_count += 1
                trajectories.append((traj, traj_available))

            if dynamic_window.min_yawrate < 0.0 and 0.0 < dynamic_window.max_yawrate:
                traj = self.generate_trajectory(v, 0.0)
                cost = self.evaluate_trajectory(traj, goal)
                costs.append(cost)
                if cost.obs_cost == float('inf'):
                    traj_available = False
                else:
                    traj_available = True
                    available_traj_count += 1
                trajectories.append((traj, traj_available))

        if available_traj_count == 0:
            rospy.logerr_throttle(1.0, "No available trajectory")
            best_traj = self.generate_trajectory(0.0, 0.0)
        else:
            self.normalize_costs(costs)
            for i, cost in enumerate(costs):
                if cost.obs_cost != float('inf'):
                    cost = Cost(cost.to_goal_cost * self.to_goal_cost_gain,
                                cost.obs_cost * self.obs_cost_gain,
                                cost.speed_cost * self.speed_cost_gain,
                                cost.path_cost * self.path_cost_gain,
                                cost.to_goal_cost * self.to_goal_cost_gain +
                                cost.obs_cost * self.obs_cost_gain +
                                cost.speed_cost * self.speed_cost_gain +
                                cost.path_cost * self.path_cost_gain)
                    if cost.total_cost < min_cost.total_cost:
                        min_cost = cost
                        best_traj = trajectories[i][0]

        rospy.loginfo("===")
        rospy.loginfo("(v, y) = (%f, %f)", best_traj[0].velocity, best_traj[0].yawrate)
        min_cost.show()
        rospy.loginfo("num of trajectories available: %d of %d", available_traj_count, len(trajectories))
        rospy.loginfo(" ")

        return best_traj
    
    def calculate_dynamic_window(self, current_cmd_vel):
        window = Window(self.min_velocity, self.max_velocity, -self.max_yawrate, self.max_yawrate)
        window.min_velocity = max((current_cmd_vel.linear.x - self.max_deceleration * self.dt), self.min_velocity)
        window.max_velocity = min((current_cmd_vel.linear.x + self.max_acceleration * self.dt), self.target_velocity)
        window.min_yawrate = max((current_cmd_vel.angular.z - self.max_d_yawrate * self.dt), -self.max_yawrate)
        window.max_yawrate = min((current_cmd_vel.angular.z + self.max_d_yawrate * self.dt), self.max_yawrate)
        return window

    def generate_trajectory(velocity: float, yawrate: float, predict_time: float, dt: float):
        trajectory_size = int(predict_time / dt)
        trajectory = [State() for _ in range(trajectory_size)]
        for state in trajectory:
            state.yaw_ += yawrate * dt
            state.x_ += velocity * math.cos(state.yaw_) * dt
            state.y_ += velocity * math.sin(state.yaw_) * dt
            state.velocity_ = velocity
            state.yawrate_ = yawrate
        return trajectory

    def evaluate_trajectory(self):
        pass