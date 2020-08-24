import re

import abstractprng
import generators

def welcome() -> None:
    print("Welcome this pseudorandom number generator, or PRNG for short!\n")

    print("Enter n to generate a number.")
    print("Enter n followed by two integers to generate a number within a "
        "specified range. Example: n -1 10 specifies a range of [-1, 10)\n")

    print("Enter s to display the current seed of your PRNG.")
    print("Enter s followed by an integer to set the seed for your PRNG. "
        "Example: s 11\n")

    print("Type exit to exit this program.\n")

def ask_user(prng: abstractprng.AbstractPRNG) -> None:
    n_re = re.compile('n (-*\d+) (-*\d+)')
    s_re = re.compile('s (-*\d+)')
    while True:
        command = input(">>> Command: ")
        n_match = n_re.match(command)
        s_match = s_re.match(command)

        if command == 'n':
            print(prng.generate())
        elif n_match:
            low, high = int(n_match.group(1)), int(n_match.group(2))
            try:
                print(prng.generate_in_range(low, high))
            except ValueError as msg:
                print(msg)
        elif command == 's':
            print(prng.get_seed())
        elif s_match:
            seed = int(s_match.group(1))
            prng.set_seed(seed)
        elif command == 'exit':
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    welcome()
    prng = generators.LinearCongruential()
    ask_user(prng)
