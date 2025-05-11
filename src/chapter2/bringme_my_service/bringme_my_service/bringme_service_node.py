import time
import rclpy
from rclpy.node import Node 
from airobot_interfaces.srv import StringCommand

class BringmeService(Node):
    def __init__(self):
        super().__init__('bringme_service')
        self.service = self.create_service(StringCommand,'command',self.callback)
        self.food = ['apple','banana','candy']

    def callback(self,request,response):
        time.sleep(5)
        item = request.command
        if item in self.food:
            response.answer = f'はい、{item}です。'
        else:
            response.answer = f'{item}を見つけることができませんでした'

        self.get_logger().info(f'レスポンス: {response.answer}')
        return response

def main():
    rclpy.init()
    bringme_service = BringmeService()
    try:
        rclpy.spin(bringme_service)
    except KeyboardInterrupt:
        pass
    rclpy.try_shutdown()
    print('server stopped')