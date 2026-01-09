#!/usr/bin/env python3
import rospy
import serial
from std_msgs.msg import Bool

class PipetteMotorNode:
    def __init__(self):
        # 打开串口 ttyACM1，波特率 9600
        port = rospy.get_param("~pipette_motor_port", "/dev/ttyACM1")
        baud = int(rospy.get_param("~pipette_motor_baud", 9600))
        try:
            self.ser = serial.Serial(port, baud, timeout=1)
            rospy.loginfo("Pipette motor connected on /dev/ttyACM1")
        except Exception as e:
            rospy.logerr(f"Failed to open serial port: {e}")
            exit(1)

        # 创建订阅者
        rospy.Subscriber('/pipette_motor/trigger', Bool, self.trigger_callback)

    def trigger_callback(self, msg):
        if msg.data:  # 如果收到 True，就执行动作
            try:
                command = '01'
                command_byte = bytes.fromhex(command)
                self.ser.write(command_byte)  # 发送字符 "1"
                rospy.loginfo(f"Sent command to pipette motor: {command_byte} (eject tip)")
            except Exception as e:
                rospy.logwarn(f"Failed to send command: {e}")

    def spin(self):
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('pipette_motor_node')
    node = PipetteMotorNode()
    node.spin()