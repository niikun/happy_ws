import sys

import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int32,String
from rclpy.executors import ExternalShutdownException

class FizzBuzzNode(Node):
    def __init__(self):
        super().__init__('fizz_buzz')
        self.pub = self.create_publisher(String,'happy_fiz_buz',10)
        self.sub = self.create_subscription(Int32,'happy_num',self.callback,10)

    def callback(self,sub_msg):
        pub_msg = String()
        self.get_logger().info(f'サブクライブ{sub_msg.data}')
        if sub_msg.data % 3 == 0 and  sub_msg.data % 5 == 0:
            pub_msg.data = f'パブリッシュ: fizz buzz'
        elif sub_msg.data %5 == 0:
            pub_msg.data = f'パブリッシュ: fizz'
        elif sub_msg.data %3 == 0:
            pub_msg.data = f'パブリッシュ: buzz'
        else:
            pub_msg.data = f'パブリッシュ: {sub_msg.data}'
        self.pub.publish(pub_msg)
        self.get_logger().info(pub_msg.data)

def main():
    rclpy.init()
    node = FizzBuzzNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)
    finally:
        node.destroy_node()
        rclpy.try_shutdown()