import argparse

import csma
import csma.parser

arg_parser = argparse.ArgumentParser(description='Simulate a simplified CSMA.')
arg_parser.add_argument('input', default='input.txt')
args = arg_parser.parse_args()

parsed = csma.parser.parse(args.input)
util, percent_idle, num_collisions, variance_success, variance_collisions = csma.main(parsed['num_nodes'],
                                                                                      parsed['packet_size'],
                                                                                      parsed['random_ranges'],
                                                                                      parsed['attempts'],
                                                                                      parsed['sim_time'])

with open('output.txt', 'w') as out_file:
    out_file.write('Channel utilization (in percentage) ' + str(util) + '\n')
    out_file.write('Channel idle fraction (in percentage) ' + str(percent_idle) + '\n')
    out_file.write('Total number of collisions ' + str(num_collisions) + '\n')
    out_file.write('Variance in number of successful transmissions (across all nodes) ' + str(variance_success) + '\n')
    out_file.write('Variance in number of collisions (across all nodes) ' + str(variance_collisions) + '\n')
