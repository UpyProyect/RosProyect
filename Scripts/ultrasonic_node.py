#!/usr/bin/env python

import rospy
import serial

from ultrasonic_module.msg import ultrasonic_data


def talker():
	talker_topic = rospy.Publisher('chatter', ultrasonic_data, queue_size = 20)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)
	msg = ultrasonic_data()
	ser = serial.Serial("/dev/ttyACM0", baudrate = 115200)

	while not rospy.is_shutdown():
		mystr = str(ser.readline())

		print(mystr)
		msg.distance = mystr

		talker_topic.publish(msg)

		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
