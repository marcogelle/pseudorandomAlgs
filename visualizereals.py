import matplotlib.pyplot as plt
import numpy as np
import generators
import random

def bucket(n: float, nums: np.ndarray) -> int:
    for i in range(nums.size - 1, -1, -1):
        if nums[i] < n:
            return i
    return RuntimeError("Number does not fall into a bucket.")

def visualize_reals() -> None:
    low, high = 0, 1
    batch = 35
    num_samples = 1400
    assert num_samples % batch == 0
    bkt_size = 0.01
    prng = generators.LinearCongruential()

    fig, axs = plt.subplots(2, 1)
    fig.tight_layout(pad=2.0)
    nums = np.arange(low, high, bkt_size)

    cnts1 = np.zeros(nums.size)
    axs[0].bar(nums, cnts1, width=bkt_size, align='edge')
    axs[0].title.set_text('Local implementation (Real Numbers)')

    cnts2 = np.zeros(nums.size)
    axs[1].bar(nums, cnts2, width=bkt_size, align='edge')
    axs[1].title.set_text("Python's random module (Real Numbers)")

    for _ in range(num_samples // batch):
        for _ in range(batch):
            n1 = prng.generate_prob_range(low, high)
            cnts1[bucket(n1, nums)] += 1

            n2 = random.uniform(low, high)
            cnts2[bucket(n2, nums)] += 1

        axs[0].bar(nums, cnts1, width=bkt_size, align='edge')
        axs[1].bar(nums, cnts2, width=bkt_size, align='edge')
        plt.pause(0.001)

    plt.show()

if __name__ == '__main__':
    visualize_reals()
