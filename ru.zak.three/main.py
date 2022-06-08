import random
import matplotlib.pyplot as plt
from math import pi

def affiliation(n):
    radius = 1.0
    meaning = 0.0
    for i in range(1, n):
        x = random.random()
        y = random.random()
        meaning += (x * x + y * y < radius)
    return (4 * meaning / n)

pi_meaning = dict()
for i in range(1000, 500000+1, 10000):
    pi_meaning[i] = affiliation(i)
    print(pi_meaning[i])

plt.plot(pi_meaning.keys(), pi_meaning.values(), linestyle = '--', marker = 'o', color = 'k', markersize = '4')
plt.axhline(pi, color = 'r')
plt.ylim(2.9, 3.3)
plt.show()


