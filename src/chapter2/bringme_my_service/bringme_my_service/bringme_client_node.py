import rclpy
from rclpy.node import Node 
from airobot_interfaces.srv import StringCommand

class BringmeClient(Node):
    def __init__(self):
        super().__init__('bringme_client_node')
        self.client = self.create_client(StringCommand,'command')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用できません。待機中・・・')
        self.request = StringCommand.Request()

    def send_request(self,order):
        self.request.command = order
        self.future = self.client.call_async(self.request)

def main():
    rclpy.init()
    bringme_client = BringmeClient()
    order = input('何を取りましょうか？')
    bringme_client.send_request(order)

    while rclpy.ok():
        rclpy.spin_once(bringme_client)
        if bringme_client.future.done():
            try:
                response = bringme_client.future.result()
            except Exception as e:
                bringme_client.get_logger().info(f'サービスの呼び出しに失敗しました。{e}')
            else:
                bringme_client.get_logger().info(
                    f'\nリクエスト:{bringme_client.request.command}-> レスポンス:{response.answer}'
                )
                break

    bringme_client.destroy_node()
    rclpy.shutdown()