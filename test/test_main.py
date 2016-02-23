import unittest

import csma


class TestMain(unittest.TestCase):
    def test_main(self):
        util, percent_idle, num_collisions, variance_success, variance_collisions = csma.main(25, 20,
                                                                                              [8, 16, 32, 64, 128], 6,
                                                                                              50000)
        print(util)
        print(percent_idle)
        print(num_collisions)
        print(variance_success)
        print(variance_collisions)


if __name__ == '__main__':
    unittest.main()
