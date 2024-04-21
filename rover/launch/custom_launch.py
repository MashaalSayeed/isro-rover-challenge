from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    package_dir = "/home/zine/rover"
    params_dir = os.path.join(package_dir, "params")

    log_level = LaunchConfiguration('log_level')
    use_rviz = LaunchConfiguration('use_rviz')

    remappings = [('/tf', 'tf'), ('/tf_static', 'tf_static')]
    use_respawn = True
    lifecycle_nodes = [
        'map_server',
        'controller_server',
        'planner_server',
        'waypoint_follower',
    ]

    declare_log_level_cmd = DeclareLaunchArgument(
        'log_level', default_value='info', description='log level'
    )

    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz', default_value='True', description='Use RViz'
    )

    configured_params = os.path.join(params_dir, "params.yaml")
    rviz_config = os.path.join(params_dir, "rviz_config.rviz")
    print(configured_params, log_level)

    return LaunchDescription([
        # Node(
        #     package='map_server_node',
        #     namespace='isro',
        #     executable='map_node',
        #     name='map',
        #     parameters=[
        #         {"yaml_filename": "/home/zine/rover/maps/isro_gmap.yaml"}
        #     ],
        # )
        declare_log_level_cmd,
        declare_use_rviz,
        Node(
            condition=IfCondition(use_rviz),
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config]
        ),
        Node(
            package='nav2_controller',
            executable='controller_server',
            output='screen',
            arguments=['--ros-args', '--params-file', configured_params, '--log-level', log_level],
            remappings=remappings
        ),
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            arguments=['--ros-args', '--params-file', configured_params, '--log-level', log_level],
            remappings=remappings,
        ),
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            arguments=['--ros-args', '--params-file', configured_params, '--log-level', log_level],
            remappings=remappings,
        ),
        Node(
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            name='waypoint_follower',
            output='screen',
            arguments=['--ros-args', '--params-file', configured_params, '--log-level', log_level],
            remappings=remappings,
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager',
            output='screen',
            parameters=[{'autostart': True, 'node_names': lifecycle_nodes}],
        ),
    ])