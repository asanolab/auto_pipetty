#!/usr/bin/env python3
import rospy
import serial
from std_msgs.msg import Bool

class PipettyMotorNode:
    def __init__(self):
        # open serial ttyACM1，baut rate 9600
        port = rospy.get_param("~pipetty_motor_port", "/dev/ttyACM1")
        baud = int(rospy.get_param("~pipetty_motor_baud", 9600))
        try:
            self.ser = serial.Serial(port, baud, timeout=1)
            rospy.loginfo("Pipetty motor connected on /dev/ttyACM1")
        except Exception as e:
            rospy.logerr(f"Failed to open serial port: {e}")
            exit(1)

        # sub
        rospy.Subscriber('/pipette_motor/trigger', Bool, self.trigger_callback)

    def trigger_callback(self, msg):
        if msg.data:  # if receive True, conduct motion
            try:
                command = '01'
                command_byte = bytes.fromhex(command)
                self.ser.write(command_byte)  # send char "1"
                rospy.loginfo(f"Sent command to pipette motor: {command_byte} (eject tip)")
            except Exception as e:
                rospy.logwarn(f"Failed to send command: {e}")

    def spin(self):
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('pipetty_motor_node')
    node = PipettyMotorNode()
    node.spin()
