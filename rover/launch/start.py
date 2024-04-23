import roslaunch

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

cli_args1 = ['map_server', 'file1.launch', 'arg1:=arg1', 'arg2:=arg2']
cli_args2 = ['pkg2', 'file2.launch', 'arg1:=arg1', 'arg2:=arg2']
cli_args3 = ['pkg3', 'file3.launch']
roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(cli_args1)
roslaunch_args1 = cli_args1[2:]

# roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(cli_args2)
# roslaunch_args2 = cli_args2[2:]

# roslaunch_file3 = roslaunch.rlutil.resolve_launch_arguments(cli_args3)

launch_files = [(roslaunch_file1, roslaunch_args1)]

parent = roslaunch.parent.ROSLaunchParent(uuid, launch_files)
parent.start()