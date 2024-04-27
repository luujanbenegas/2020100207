#!/usr/bin/env python
# -- coding: utf-8 --
import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('move_turtle', anonymous=True)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    twist = Twist()
    
    # Configura las velocidades
    twist.linear.x = 2.0
    twist.angular.z = 0.5

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        pub.publish(twist)
        
        rate.sleep()

if _name_ == '_main_':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass