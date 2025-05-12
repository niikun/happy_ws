import rclpy
from rclpy.node import Node 
from rclpy.action import ActionClient
from airobot_interfaces.action import StringCommand

class BringmeActionClient(Node):
    def __init__(self):
        super().__init__('bringme_action_client')
        self.action_client = ActionClient(self,StringCommand,'command')

    def send_goal(self,order):
        goal_msg = StringCommand.Goal()
        goal_msg.command = order
        self.action_client.wait_for_server()
        return self.action_client.send_goal_async(
            goal_msg,feedback_callback=self.feedback_callback
        )
    
    def feedback_callback(self,feedback_msg):
        self.get_logger().info(f'フィードバック受信中: 残り {feedback_msg.feedback.process}[s]')


def main():
    rclpy.init()
    bringme_action_client = BringmeActionClient()
    order = input('何を取ってきますか？')
    future = bringme_action_client.send_goal(order)
    rclpy.spin_until_future_complete(bringme_action_client,future)
    goal_handle = future.result()

    if not goal_handle.accepted:
        bringme_action_client.get_logger().info('ゴールは拒否されました')
    else:
        bringme_action_client.get_logger().info('ゴールが承認されました')
        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(bringme_action_client,result_future)
        result = result_future.result().result
    bringme_action_client.destroy_node()
    rclpy.shutdown() 