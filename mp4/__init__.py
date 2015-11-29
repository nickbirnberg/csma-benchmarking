import statistics

from .node import Node


def main(num_nodes, packet_size, random_ranges, attempts, sim_time):
    # keep track of utilization
    num_idle = 0
    num_collisions = 0
    # set Node class variables
    Node.max_attempts = attempts
    Node.random_ranges = random_ranges
    # create nodes
    all_nodes = []
    for _ in range(num_nodes):
        all_nodes.append(Node())
    # simulate
    clock = 0
    while clock < sim_time:
        # check if any nodes that can transmit now.
        ready_to_transmit = []
        for a_node in all_nodes:
            if a_node.can_transmit():
                ready_to_transmit.append(a_node)
        # transmit if only 1 node needs to
        if len(ready_to_transmit) == 1:
            ready_to_transmit.pop().send_packet()
            clock += packet_size
            continue
        # collisions
        if len(ready_to_transmit) > 1:
            num_collisions += 1
            for colliding_node in ready_to_transmit:
                colliding_node.collision()
        # idle channel
        else:
            num_idle += 1
            for a_node in all_nodes:
                a_node.tick()
        clock += 1

    utilization = (sim_time - num_collisions - num_idle) / sim_time * 100
    percent_idle = (num_idle / sim_time) * 100
    variance_success = statistics.pvariance([a_node.num_transmits for a_node in all_nodes])
    variance_collisions = statistics.pvariance([a_node.num_collisions for a_node in all_nodes])
    return utilization, percent_idle, num_collisions, variance_success, variance_collisions
