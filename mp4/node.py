import random


class Node:
    random_ranges = []
    max_attempts = 0

    def __init__(self):
        if len(self.random_ranges) == 0 or self.max_attempts == 0:
            raise RuntimeError
        self.current_attempt = 0  # attempts are 0-indexed
        self.current_r = self.random_ranges[0]
        self.back_off = random.randint(0, self.current_r)
        self.num_collisions = 0
        self.num_transmits = 0

    def can_transmit(self):
        if self.back_off == 0:
            return True
        else:
            return False

    def tick(self):
        self.back_off -= 1

    def collision(self):
        self.num_collisions += 1
        self.current_attempt += 1
        if self.current_attempt < self.max_attempts:
            if self.current_attempt >= len(self.random_ranges):
                self.current_r *= 2
            else:
                self.current_r = self.random_ranges[self.current_attempt]
            self.back_off = random.randint(0, self.current_r)
        else:
            self.reset_packet()

    def send_packet(self):
        self.num_transmits += 1
        self.reset_packet()

    def reset_packet(self):
        self.current_attempt = 0
        self.current_r = self.random_ranges[0]
        self.back_off = random.randint(0, self.current_r)
