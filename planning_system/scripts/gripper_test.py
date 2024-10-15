#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

def control_gripper(state):
    rospy.init_node('gripper_controller', anonymous=True)
    pub = rospy.Publisher('Gripper_control', Bool, queue_size=10)
    rate = rospy.Rate(10)  # 10 Гц

    gripper_msg = Bool()
    gripper_msg.data = state

    rospy.loginfo(f"Sending command to gripper: {'close' if state else 'open'}")
    pub.publish(gripper_msg)
    rate.sleep()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            user_input = input("Enter 1 to close the gripper, 0 to open it: ")
            if user_input == '1':
                control_gripper(True)
            elif user_input == '0':
                control_gripper(False)
            else:
                rospy.logwarn("Invalid command. Use 1 to close and 0 to open.")
    except rospy.ROSInterruptException:
        pass
