import time

class AbstractPRNG:
    """An abstract class for pseudorandom number generators."""

    def __init__(self) -> None:
        self.seed = round(time.time() * 1000)
        self.x = self.seed

    def generate(self) -> int:
        """Generates and returns a pseudorandom number."""
        pass

    def generate_in_range(self, low: int, high: int) -> int:
        """Generates a number within the specified range. Low is inclusive and
        high is exclusive. """
        if low >= high:
            raise ValueError("Invalid range.")

        num = generate()
        width = high - low
        return (num % width) + low

    def set_seed(self, seed: int) -> None:
        """Sets the seed for this generator."""
        self.seed = seed
        self.x = self.seed

    def get_seed(self) -> int:
        """Returns the seed currently used by this prng."""
        return self.seed
