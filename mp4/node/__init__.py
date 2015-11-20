import random


class Node:
    random_ranges = []
    max_attempts = 0
    channel_occupied = False

    def __init__(self):
        if len(self.random_ranges) == 0 or self.max_attempts == 0:
            raise RuntimeError
        self.current_attempt = 0  # attempts are 0-indexed
        self.back_off = random.randint(0, self.random_ranges[0])

    def tick(self):
        if self.back_off == 0:
            if self.channel_occupied:
                self.collision()
            else:
                self.send_packet()
        elif not self.channel_occupied:
            self.back_off -= 1
        return self.channel_occupied

    def collision(self):
        self.current_attempt += 1
        if self.current_attempt < self.max_attempts:
            # TODO: Wait for Piazza answer for what to do when current_attempt > len(random_ranges)
            self.back_off = random.randint(0, self.random_ranges[self.current_attempt])
        else:
            self.reset_packet()

    def send_packet(self):
        Node.channel_occupied = True
        self.reset_packet()

    def reset_packet(self):
        self.current_attempt = 0
        self.back_off = random.randint(0, self.random_ranges[0])
