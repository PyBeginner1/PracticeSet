import random
import numpy as np
import matplotlib.pyplot as plt

#move up or down(x or y)
prob = [0.05, 0.10]

#Starting Position is set here to 2
start = 2
positions = [start]

#Creating random points
rand = np.random.random(1000)
up = rand > prob[1]
down = rand < prob[0]

for ups,downs in zip(up, down):
    up = ups and positions[-1] < 4
    down = downs and positions[-1] > 1
    positions.append(positions[-1] -down + up)

#Plotting
plt.plot(positions)
plt.show()