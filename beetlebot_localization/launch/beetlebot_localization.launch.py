from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


nav2_yaml = os.path.join(get_package_share_directory('beetlebot_navigation'), 'config', 'beetlebot_amcl.yaml')

map_file=os.path.join(get_package_share_directory('beetlebot_navigation'), 'map', 'warehouse_map.yaml')

configuration_basename = 'beetlebot_2d.lua'
def generate_launch_description():
    return LaunchDescription([


        Node(

            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'use_sim_time': True}, 
                        {'yaml_filename':map_file} 
                       ]),

        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[nav2_yaml]
                       ),


        Node(

            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_mapper',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'node_names': ['map_server', 'amcl']}])

    ])

