import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class HappyPublisher(Node):
    def __init__(self):
        super().__init__('happy_pubisher_node')
        self.pub = self.create_publisher(String,'topic',10)
        self.timer = self.create_timer(1,self.timer_callback)
        self.i = 10

    def timer_callback(self):
        msg = String()
        if self.i > 0:
            msg.data = f'ハッピーカウントダウン{self.i}'
        elif self.i == 0:
            msg.data = f'niikun 発射！'
        else:
            msg.data = f'経過時間{- self.i}'

        self.pub.publish(msg)
        self.get_logger().info(f'パプリッシュ：{msg.data}')
        self.i -= 1

def main(arg=None):
    rclpy.init()
    node = HappyPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('CTRL + C が押されました')
    node.destroy_node()
    rclpy.try_shutdown()

