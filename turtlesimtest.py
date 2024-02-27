#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('move_turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # Create a Twist message to move the turtle forward
        move_cmd = Twist()
        move_cmd.linear.x = 1.0  # linear velocity
        move_cmd.angular.z = 0.0  # angular velocity

        # Publish the Twist message
        pub.publish(move_cmd)

        # Sleep to maintain the desired rate
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
