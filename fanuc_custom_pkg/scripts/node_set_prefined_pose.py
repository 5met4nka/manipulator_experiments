#! /usr/bin/python3

# Python 2/3 compatibility imports
from __future__ import print_function
from six.moves import input

# Include the necessary libraries
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
from std_msgs.msg import Bool  # импортируем Bool для управления захватом

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi
    
    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class MyRobot:

    # Default Constructor
    def __init__(self, Group_Name):
        # Initialize the moveit_commander and rospy node
        self._commander = moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('node_set_predefined_pose', anonymous=True)

        # Instantiate a RobotCommander object
        self._robot = moveit_commander.RobotCommander()
        self._scene = moveit_commander.PlanningSceneInterface()
        
        # Define the move group for the robotic arm
        self._planning_group = Group_Name
        self._group = moveit_commander.MoveGroupCommander(self._planning_group)
        
        # Create a DisplayTrajectory ROS publisher
        self._display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
        
        # Create action client for the "Execute Trajectory" action server
        self._exectute_trajectory_client = actionlib.SimpleActionClient('execute_trajectory', moveit_msgs.msg.ExecuteTrajectoryAction)
        self._exectute_trajectory_client.wait_for_server()

        # Get the planning frame, end effector link and the robot group names
        self._planning_frame = self._group.get_planning_frame()
        self._eef_link = self._group.get_end_effector_link()
        self._group_names = self._robot.get_group_names()

        # Initialize gripper publisher
        self._gripper_pub = rospy.Publisher('/Gripper_control', Bool, queue_size=1)

        rospy.loginfo('\033[95m' + "Planning Group: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo('\033[95m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo('\033[95m' + "Group Names: {}".format(self._group_names) + '\033[0m')
        rospy.loginfo('\033[95m' + " >>> MyRobot initialization is done." + '\033[0m')

    def set_pose(self, arg_pose_name):
        rospy.loginfo('\033[32m' + "Going to Pose: {}".format(arg_pose_name) + '\033[0m')
        self._group.set_named_target(arg_pose_name)
        plan_success, plan, planning_time, error_code = self._group.plan()
        goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
        goal.trajectory = plan
        self._exectute_trajectory_client.send_goal(goal)
        self._exectute_trajectory_client.wait_for_result()
        rospy.loginfo('\033[32m' + "Now at Pose: {}".format(arg_pose_name) + '\033[0m')

    def control_gripper(self, state):
        # Публикация состояния захвата (True для закрытия, False для открытия)
        self._gripper_pub.publish(Bool(data=state))
        if state:
            rospy.loginfo('\033[32m' + "Gripper closed." + '\033[0m')
        else:
            rospy.loginfo('\033[32m' + "Gripper opened." + '\033[0m')

    # Class Destructor
    def __del__(self):
        moveit_commander.roscpp_shutdown()
        rospy.loginfo('\033[95m' + "Object of class MyRobot Deleted." + '\033[0m')


def main():
    arm = MyRobot("manipulator")
    arm.set_pose("all-zeros")
    rospy.sleep(1)

    while not rospy.is_shutdown():
        # Go to Lift Object Pose
        arm.set_pose("1")
        rospy.sleep(1)

        # Close the gripper (захват объекта)
        arm.control_gripper(True)
        rospy.sleep(1)

        # Go to Pick Object Pose
        arm.set_pose("2")
        rospy.sleep(1)
        
        # Go to drop Object Pose
        arm.set_pose("3")
        rospy.sleep(1)

        # Open the gripper (освобождение объекта)
        arm.control_gripper(False)
        rospy.sleep(1)

    del arm

if __name__ == '__main__':
    main()

# <group_state name="all-zeros" group="manipulator">
#     <joint name="joint_1" value="0" />
#     <joint name="joint_2" value="0" />
#     <joint name="joint_3" value="0" />
#     <joint name="joint_4" value="0" />
#     <joint name="joint_5" value="0" />
#     <joint name="joint_6" value="0" />
# </group_state>
# <group_state name="1" group="manipulator">
#     <joint name="joint_1" value="0" />
#     <joint name="joint_2" value="0.9894589185714722" />
#     <joint name="joint_3" value="-0.2641632556915283" />
#     <joint name="joint_4" value="0" />
#     <joint name="joint_5" value="-0.2852860689163208" />
#     <joint name="joint_6" value="0" />
# </group_state>
# <group_state name="2" group="manipulator">
#     <joint name="joint_1" value="0" />
#     <joint name="joint_2" value="0.8440462946891785" />
#     <joint name="joint_3" value="0.12622225284576416" />
#     <joint name="joint_4" value="0" />
#     <joint name="joint_5" value="1.14151930809021" />
#     <joint name="joint_6" value="0" />
# </group_state>
# <group_state name="3" group="manipulator">
#     <joint name="joint_1" value="0.6339782476425171" />
#     <joint name="joint_2" value="0.7194051146507263" />
#     <joint name="joint_3" value="0.33129793405532837" />
#     <joint name="joint_4" value="0.03839888423681259" />
#     <joint name="joint_5" value="-1.1603854894638062" />
#     <joint name="joint_6" value="0" />
# </group_state>