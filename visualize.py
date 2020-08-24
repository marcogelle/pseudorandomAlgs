import matplotlib.pyplot as plt
import generators
import random

low, high = -35, 35
batch = 25
num_samples = 1000
assert num_samples % batch == 0

fig, (ax1, ax2) = plt.subplots(2)
fig.tight_layout(pad=2.0)
nums = [n for n in range(low, high)]

cnts1 = [0] * len(nums)
ax1.bar(nums, cnts1)
ax1.title.set_text('Local implementation of LCG')

cnts2 = [0] * len(nums)
ax2.bar(nums, cnts2)
ax2.title.set_text("Python's random module")

prng = generators.LinearCongruential()
for _ in range(num_samples // batch):
    for _ in range(batch):
        n1 = prng.generate_in_range(low, high)
        cnts1[n1 - low] += 1

        n2 = random.randrange(low, high)
        cnts2[n2 - low] += 1

    ax1.bar(nums, cnts1)
    ax2.bar(nums, cnts2)
    plt.pause(0.001)

plt.show()
