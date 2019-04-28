#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import time
import math



def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    z = data.data.split(',')
    x1 = float(z[][])    #Fill with appropriate data cells of node data
    y1 = float(z[][])    #Fill with appropriate data cells of node data

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    z = data.data.split(',')
    x2 = float(z[][])    #Fill with appropriate data cells of node data
    y2 = float(z[][])    #Fill with appropriate data cells of node data
def pose():
    rospy.init_node('calculator', anonymous = True)
    rospy.Subscriber("hedge1", String, callback1)  #Replace hedge 1 and 2 with actual ids...
    rospy.Subscriber("hedge2", String, callback2)
    pub = rospy.Publisher("robot_pose", Float32)

    rospy.rate(10)     #Sets rate of pose to 10 Hz
    if x2 > x1 :  #Quadrant1 and 4: atan() works from -90 to 90
        pose = math.atan( (y2 - y1)/(x2 - x1) )
    if x2 < x1:   #Quadrant2 and 3
        pose = math.atan( (x1 - x2)/(x2 - x1) )
    
    pub.publish(pose)
    rate.sleep()

    rospy.spin()    #loops
if __name__ == '__main__':
   x1 = 0
   x2 = 0
   y1 = 0
   y2 = 0
   pose = 0.0
   pose()