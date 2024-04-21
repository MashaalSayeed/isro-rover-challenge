from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    log_level = LaunchConfiguration('log_level')
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

    configured_params = os.path.join("/home/zine/rover", "params", "nav2_params.yaml")

    bringup_cmd_group = GroupAction([
        # Node(
        #     package='map_server_node',
        #     namespace='isro',
        #     executable='map_node',
        #     name='map',
        #     parameters=[
        #         {"yaml_filename": "/home/zine/launch/isro_map.yaml"}
        #     ]
        # ),
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            respawn=use_respawn,
            respawn_delay=2.0,
            parameters=[configured_params, {'yaml_filename': "/home/zine/rover/maps/isro_gmap.yaml"}],
            arguments=['--ros-args', '--log-level', log_level],
            remappings=remappings,
        ),
        Node(
            package='nav2_controller',
            executable='controller_server',
            output='screen',
            respawn=use_respawn,
            respawn_delay=2.0,
            parameters=[configured_params],
            arguments=['--ros-args', '--log-level', log_level],
            remappings=remappings + [('cmd_vel', 'cmd_vel_nav')],
        ),
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            respawn=use_respawn,
            respawn_delay=2.0,
            parameters=[configured_params],
            arguments=['--ros-args', '--log-level', log_level],
            remappings=remappings,
        ),
        Node(
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            name='waypoint_follower',
            output='screen',
            respawn=use_respawn,
            respawn_delay=2.0,
            parameters=[configured_params],
            arguments=['--ros-args', '--log-level', log_level],
            remappings=remappings,
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            arguments=['--ros-args', '--log-level', log_level],
            parameters=[{'autostart': False}, {'node_names': lifecycle_nodes}],
        ),
    ])

    ld = LaunchDescription()
    ld.add_action(DeclareLaunchArgument(
        'autostart',
        default_value='true',
        description='Automatically startup the nav2 stack',
    ))

    ld.add_action(declare_log_level_cmd)
    ld.add_action(bringup_cmd_group)

    return ld