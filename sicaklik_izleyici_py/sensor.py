import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor')
        self.publisher_ = self.create_publisher(Float32, '/sicaklik', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        self.get_logger().info('Sıcaklık Sensör Düğümü Başlatıldı.')

    def publish_temperature(self):
        msg = Float32()
        msg.data = random.uniform(20.0, 40.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlanan Sıcaklık: {msg.data:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
