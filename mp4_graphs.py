import matplotlib.pyplot as plt

import mp4

# part A + B + C

channel_utilization = []
idle_fraction = []
total_collisions = []
for n in range(5, 101):
    percent_idle, num_collisions, variance_success, variance_collisions = mp4.main(n, 20, [8, 16, 32, 64, 128], 6,
                                                                                   50000)
    channel_utilization.append(100 - percent_idle)
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

plt.show()
