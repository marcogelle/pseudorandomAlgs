import matplotlib.pyplot as plt
import generators
import random

low, high = 0, 15

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
nums = [n for n in range(low, high)]
cnts = [0] * len(nums)
ax.bar(nums, cnts)

prng = generators.LinearCongruential()
for _ in range(150):
    n = prng.generate_in_range(low, high)
    # n2 = random.randrange(low, high)
    cnts[n - low] += 1
    ax.bar(nums, cnts)
    plt.pause(0.001)

plt.show()
