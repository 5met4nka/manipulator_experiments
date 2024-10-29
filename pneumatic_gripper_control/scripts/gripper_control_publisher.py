#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

def gripper_control_publisher():
    # Инициализация узла
    rospy.init_node('gripper_control_publisher', anonymous=True)
    
    # Создание паблишера для топика /Gripper_control
    pub = rospy.Publisher('/Gripper_control', Bool, queue_size=10)
    
    # Установка частоты публикации 1 Гц
    rate = rospy.Rate(1)  # 1 Гц
    
    while not rospy.is_shutdown():
        # Создание сообщения
        msg = Bool()
        
        # Чередование значений True и False
        msg.data = True if rospy.get_time() % 2 < 1 else False
        
        # Публикация сообщения
        pub.publish(msg)
        rospy.loginfo(f'Published: {msg.data}')
        
        # Ожидание следующего цикла
        rate.sleep()

if __name__ == '__main__':
    try:
        gripper_control_publisher()
    except rospy.ROSInterruptException:
        pass