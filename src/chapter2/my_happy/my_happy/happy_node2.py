import rclpy
from rclpy.node import Node

class HappyNode2(Node):
    def __init__(self):
        print('ノードの生成')
        super().__init__('happy_node2')
        self.timer = self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('ハッピーワールド')

def main():
    print('program starts')
    rclpy.init()
    node = HappyNode2()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('Ctrl+C が押されました')
    node.destroy_node()
    rclpy.try_shutdown()
    print('program ends')