import unittest

from csma import parser


class TestParser(unittest.TestCase):
    def test_parse_input(self):
        parsed = parser.parse('input.txt')
        expected = {'num_nodes': 25, 'packet_size': 20, 'random_ranges': [8, 16, 32, 64, 128],
                    'attempts': 6, 'sim_time': 50000}
        self.assertDictEqual(parsed, expected)


if __name__ == '__main__':
    unittest.main()
