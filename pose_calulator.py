#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import time
import math



def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    if counter == 0: #if first values not assigned:
        z = data.data.split(',')
        x1 = float(z[][])    #Fill with appropriate data cells of node data
        y1 = float(z[][])    #Fill with appropriate data cells of node data
        counter = counter + 1
    else:           #assign second values
    	z = data.data.split(',')
        x2 = float(z[][])    #Fill with appropriate data cells of node data
        y2 = float(z[][])    #Fill with appropriate data cells of node data
        counter = 0
        ready = True



def pose():
    rospy.init_node('calculator', anonymous = True)
    rospy.Subscriber("hedge", String, callback1)  #Replace hedge 1 and 2 with actual ids...
    pub = rospy.Publisher("robot_pose", Float32)

    rospy.rate(250)     #Sets rate of pose to 250 Hz faster than hedge output single message rate. only publishes when boolean is true

    if counter == 0 and ready is True:
    	ready = False
        if x2 >= x1 and y2 >= y1 :  #Quadrant1 output [0-90]
            pose = math.atan( (y2 - y1)/(x2 - x1) )
        if x2 >= x1 and y2 < y1:  #Quadrant4 output [270,360)
            pose = 360 + math.atan( (y2 - y1)/(x2 - x1) )    
        if x2 < x1 and y2 >= y1:   #Quadrant2 output (90,180]
            pose = 180 + math.atan( (y2 - y1)/(x2 - x1) ) 
        if x2 < x1 and y2 < y1:    #Quadrant3 output (180,270)
    	    pose = 180 + math.atan( (y2 - y1)/(x2 - x1) )
        pub.publish(pose)

    rate.sleep()
    rospy.spin()    #loops
if __name__ == '__main__':
   x1 = 0
   x2 = 0
   y1 = 0
   y2 = 0
   pose = 0.0
   ready = False
   pose()