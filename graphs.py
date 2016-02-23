import matplotlib.pyplot as plt

import csma

# part A + B + C

channel_utilization = []
idle_fraction = []
total_collisions = []
for n in range(5, 101):
    util, percent_idle, num_collisions, _, _ = csma.main(n, 20, [8, 16, 32, 64, 128], 6, 50000)
    channel_utilization.append(util)
    idle_fraction.append(percent_idle)
    total_collisions.append(num_collisions)

# A
plt.figure(1)
plt.plot(range(5, 101), channel_utilization)
plt.xlabel('Number of Nodes (N)')
plt.ylabel('Channel Utilization (%)')
plt.title('A')
# B
plt.figure(2)
plt.plot(range(5, 101), idle_fraction)
plt.xlabel('Number of Nodes (N)')
plt.ylabel('Channel Idle Fraction (%)')
plt.title('B')
# C
plt.figure(3)
plt.plot(range(5, 101), total_collisions)
plt.xlabel('Number of Nodes (N)')
plt.ylabel('Number of Collisions')
plt.title('C')

# D
plt.figure(4)
for r in [1, 2, 4, 8, 16]:
    channel_utilization = []
    for n in range(5, 101):
        util, percent_idle, _, _, _ = csma.main(n, 20, [r], 6, 50000)
        channel_utilization.append(util)
    plt.plot(range(5, 101), channel_utilization, hold=True, label='R =' + str(r))
plt.xlabel('Number of Nodes (N)')
plt.ylabel('Channel Utilization (%)')
plt.legend(loc=3)
plt.title('D')

# E
plt.figure(5)
for l in [20, 40, 60, 80, 100]:
    channel_utilization = []
    for n in range(5, 101):
        util, percent_idle, _, _, _ = csma.main(n, l, [8, 16, 32, 64, 128], 6, 50000)
        channel_utilization.append(util)
    plt.plot(range(5, 101), channel_utilization, hold=True, label='L =' + str(l))
plt.xlabel('Number of Nodes (N)')
plt.ylabel('Channel Utilization (%)')
plt.legend(loc=3)
plt.title('E')

plt.show()
