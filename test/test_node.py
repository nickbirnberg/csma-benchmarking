import unittest

from mp4 import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        Node.channel_occupied = False
        Node.random_ranges = []
        Node.max_attempts = 0

    def test_node_creation(self):
        with self.assertRaises(RuntimeError):
            node_a = Node()
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 10
        node_a = Node()
        self.assertIsInstance(node_a, Node)

    def test_tick(self):
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 10
        node_a = Node()
        node_a.back_off = 1
        node_b = Node()
        node_b.back_off = 1
        node_c = Node()
        node_c.back_off = 2

        node_a.tick()
        node_b.tick()
        node_c.tick()
        self.assertEqual(node_a.back_off, 0)
        self.assertEqual(node_b.back_off, 0)
        self.assertEqual(node_c.back_off, 1)

        node_a.tick()
        node_b.tick()
        node_c.tick()
        self.assertEqual(node_b.current_attempt, 1)
        self.assertEqual(node_c.back_off, 1)
        self.assertEqual(node_a.num_transmits, 1)
        node_b.back_off = 0

        node_b.tick()
        node_c.tick()
        self.assertEqual(node_b.current_attempt, 2)
        self.assertEqual(node_c.back_off, 1)

        Node.channel_occupied = False
        node_a.tick()
        node_b.tick()
        node_c.tick()
        self.assertEqual(node_c.back_off, 0)

    def test_collision(self):
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 3
        node_a = Node()
        node_a.collision()
        self.assertEqual(node_a.current_attempt, 1)
        node_a.collision()
        self.assertEqual(node_a.current_attempt, 2)
        node_a.collision()
        self.assertEqual(node_a.current_attempt, 0)
        self.assertEqual(node_a.num_collisions, 3)

    def test_send_packet(self):
        Node.random_ranges = [8, 16, 32]
        Node.max_attempts = 3
        node_a = Node()
        node_b = Node()
        node_a.current_attempt = 2
        node_a.back_off = 0
        node_a.send_packet()
        self.assertEqual(node_a.current_attempt, 0)
        self.assertEqual(node_b.channel_occupied, True)
        self.assertEqual(node_a.num_transmits, 1)


if __name__ == '__main__':
    unittest.main()
