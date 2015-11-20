import unittest

import mp4


class TestMain(unittest.TestCase):
    def test_main(self):
        percent_idle, num_collisions, variance_success, variance_collisions = mp4.main(25, 20, [8, 16, 32, 64, 128], 6,
                                                                                       50000)
        print(percent_idle)
        print(num_collisions)
        print(variance_success)
        print(variance_collisions)


if __name__ == '__main__':
    unittest.main()