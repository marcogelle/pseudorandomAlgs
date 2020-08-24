import generators

def welcome() -> None:
    print("Welcome this pseudorandom number generator!\n")

    print("Enter n to generate a number.")
    print("Enter n followed by two integers to generate a number within a"
        "specified range. Example: n 1 10 specifies a range of [1, 10)\n")

    print("Enter s to display the current seed of your PRNG.")
    print("Enter s followed by an integer to set the seed for your PRNG."
        "Example: s 11\n")

    print("Type exit to exit this program.\n")

def ask_user(prnb: abstractprng.AbstractPRNG) -> None:
    while True:
        command = input("Command: ")
        if command == 'n':
            print(prng.generate())
        elif command == 's':
            print(prng.get_seed())
        elif command == 'exit':
            break
        else:
            try:
                seed = int(command)
                prng.set_seed(seed)
            except ValueError:
                print('Invalid command')

if __name__ == '__main__':
    welcome()
    prng = lcg.LinearCongruential()
    ask_user(prng)
