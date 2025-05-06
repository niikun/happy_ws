import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class HappySubscriber(Node):
    def __init__(self):
        super().__init__('happy_sbscriber_node')
        self.sub = self.create_subscription(
            String,'topic',self.callback,10
        )

    def callback(self,msg):
        self.get_logger().info(f'subscribe {msg.data}')

def main():
    rclpy.init()
    node = HappySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print(' Ctrl + C が押されました。')
    node.destroy_node()
    rclpy.try_shutdown()