#! /usr/bin/env python

import rospy
from std_msgs.msg import String             # Import the String message from the std_msgs package

rospy.init_node("Topic_publisher")

pub = rospy.Publisher('message', String) 

rate = rospy.Rate(2) # We create a Rate object of 2Hz

phrase = String("Hello World")             # Create a var of type String


while not rospy.is_shutdown(): # Endless loop until Ctrl + C
   pub.publish(phrase)                       # Publish the message within the 'phrase' variable
   rate.sleep() # We sleep the needed time to maintain the Rate fixed above
# This program creates an endless loop that repeats itself 2 times per second (2Hz) until somebody presses Ctrl + C in the Shell
