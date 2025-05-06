import rclpy
from rclpy.node import Node 
from std_msgs.msg import String
import datetime

class HappyTime(Node):
    def __init__(self):
        super().__init__('happy_time')
        self.pub = self.create_publisher(String,'time',10)
        self.timer = self.create_timer(1,self.time_callback)

    def time_callback(self):
        time_now = datetime.datetime.now().strftime('%Y/%m/%d/%H/%M/%S')
        msg = String()
        msg.data = f'只今の時間は...{time_now}'
        self.pub.publish(msg)
        self.get_logger().info(f'publish {msg.data}')

def main():
    rclpy.init()
    node = HappyTime()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print(" Ctrl + C が押されました")
    node.destroy_node()
    rclpy.try_shutdown()