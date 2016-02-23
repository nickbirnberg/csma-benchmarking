import unittest

from csma import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        Node.random_ranges = []
        Node.max_attempts = 0

    def test_node_creation(self):
        with self.assertRaises(RuntimeError):
            node_a = Node()
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 10
        node_a = Node()
        self.assertIsInstance(node_a, Node)

    def test_can_transmit(self):
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 10
        node_a = Node()
        node_a.back_off = 1
        node_b = Node()
        node_b.back_off = 3

        self.assertEqual(node_a.can_transmit(), False)
        self.assertEqual(node_b.can_transmit(), False)

        node_a.tick()
        node_b.tick()
        self.assertEqual(node_a.can_transmit(), True)
        self.assertEqual(node_b.can_transmit(), False)

    def test_collision(self):
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 4
        node_a = Node()
        node_a.collision()
        self.assertEqual(node_a.current_attempt, 1)
        node_a.collision()
        self.assertEqual(node_a.current_attempt, 2)
        node_a.collision()
        self.assertEqual(node_a.current_attempt, 3)
        self.assertEqual(node_a.current_r, 64)
        node_a.collision()
        self.assertEqual(node_a.num_collisions, 4)
        self.assertEqual(node_a.current_attempt, 0)

    def test_send_packet(self):
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 3
        node_a = Node()
        node_a.current_attempt = 2
        node_a.back_off = 0
        node_a.send_packet()
        self.assertEqual(node_a.current_attempt, 0)
        self.assertEqual(node_a.num_transmits, 1)


if __name__ == '__main__':
    unittest.main()
