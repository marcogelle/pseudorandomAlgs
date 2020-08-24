from abstractprng import AbstractPRNG

class LinearCongruential(AbstractPRNG):
    """Implementing a linear congruential generator."""
    # Using parameters from ANSI C implementation
    m = 1 << 32
    a = 1103515245
    c = 12345

    def generate(self) -> int:
        self.x = (LinearCongruential.a * self.x + LinearCongruential.c) % LinearCongruential.m
        return self.x
