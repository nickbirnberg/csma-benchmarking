import statistics

from mp4.node import Node


def main(num_nodes, packet_size, random_ranges, attempts, sim_time):
    # keep track of utilization
    num_idle = 0
    # set Node class variables
    Node.max_attempts = attempts
    Node.random_ranges = random_ranges
    # create nodes
    all_nodes = []
    for _ in range(num_nodes):
        all_nodes.append(Node())
    # s(t)imulation!
    all_nodes.sort(key=lambda a_node: a_node.back_off)
    clock = 0
    while clock < sim_time:
        Node.channel_occupied = False
        for a_node in all_nodes:
            if a_node.tick():
                clock += packet_size
        all_nodes.sort(key=lambda a_node: a_node.back_off)
        if not Node.channel_occupied:
            num_idle += 1
            clock += 1

    percent_idle = (num_idle / sim_time) * 100
    collisions_list = [a_node.num_collisions for a_node in all_nodes]
    num_collisions = sum(collisions_list)
    variance_success = statistics.pvariance([a_node.num_transmits for a_node in all_nodes])
    variance_collisions = statistics.pvariance(collisions_list)

    return percent_idle, num_collisions, variance_success, variance_collisions
