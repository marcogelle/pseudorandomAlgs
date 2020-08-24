import matplotlib.pyplot as plt
import numpy as np
import generators
import random

low, high = -35, 35
batch = 25
num_samples = 1000
assert num_samples % batch == 0
prng = generators.LinearCongruential()

fig, axs = plt.subplots(2, 1)
fig.tight_layout(pad=2.0)
nums = np.arange(low, high)

cnts1 = np.zeros(nums.size)
axs[0].bar(nums, cnts1)
axs[0].title.set_text('Local implementation (Integers)')

cnts2 = np.zeros(nums.size)
axs[1].bar(nums, cnts2)
axs[1].title.set_text("Python's random module (Integers)")

for _ in range(num_samples // batch):
    for _ in range(batch):
        n1 = prng.generate_in_range(low, high)
        cnts1[n1 - low] += 1

        n2 = random.randrange(low, high)
        cnts2[n2 - low] += 1

    axs[0].bar(nums, cnts1)
    axs[1].bar(nums, cnts2)
    plt.pause(0.001)

plt.show()
