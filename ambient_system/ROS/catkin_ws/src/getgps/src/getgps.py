#!/usr/bin/env python
import gi
gi.require_version('Geoclue', '2.0')
import rospy
from sensor_msgs.msg import NavSatFix
from gi.repository import Geoclue
clue = Geoclue.Simple.new_sync('something',Geoclue.AccuracyLevel.NEIGHBORHOOD,None)
location = clue.get_location()
#print(location.get_property('latitude'), location.get_property('longitude'))

rospy.init_node('gps_publisher')
pub = rospy.Publisher('/gps', NavSatFix, queue_size=10)

rate = rospy.Rate(10)  # 10 Hz

while not rospy.is_shutdown():
    # TODO: get latitude, longitude, and altitude data from GPS receiver
    latitude = location.get_property('latitude')
    longitude = location.get_property('longitude')
    altitude = 0.0

        # Create NavSatFix message
    msg = NavSatFix()
    msg.header.stamp = rospy.Time.now()
    msg.latitude = latitude
    msg.longitude = longitude
    msg.altitude = altitude
    #rospy.loginfo(msg)
    # Publish message
    pub.publish(msg)

    rate.sleep()


