import rclpy
from rclpy.node import Node

class HappyNode(Node):
    def __init__(self):
        print("ノードができた")
        super().__init__('happy_node')
        self.get_logger().info('ハッピーワールド!!!')

def main():
    print('プログラム開始')
    rclpy.init()
    node = HappyNode()
    node.destroy_node()
    rclpy.shutdown()
    print('終了！')