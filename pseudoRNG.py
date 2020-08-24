class PseudoRNG:
    """An abstract class for pseudorandom number generators."""
    
    def __init__(self, seed = 0: int):
        self.seed = seed

    def generate(self) -> int:
        """Generates and returns a pseudorandom number."""
        pass

    def set_seed(self, seed: int) -> int:
        """Sets the seed for this generator"""
        self.seed = seed
