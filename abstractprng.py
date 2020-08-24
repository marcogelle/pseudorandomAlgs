import time

class AbstractPRNG(metaclass=abc.ABCMeta):
    """An abstract class for pseudorandom number generators."""

    def __init__(self):
        self.seed = round(time.time() * 1000)
        self.x = self.seed

    def generate(self) -> int:
        """Generates and returns a pseudorandom number."""
        pass

    def set_seed(self, seed: int) -> int:
        """Sets the seed for this generator"""
        self.seed = seed
        self.x = self.seed

    def get_seed(self) -> int:
        return self.seed
