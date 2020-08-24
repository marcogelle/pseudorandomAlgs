import generators

def welcome() -> None:
    print("Welcome this pseudorandom number generator!")
    print("Enter n to generate a number")
    print("Enter s to display the current seed of your PRNG")
    print("Type exit to exit this program")
    print()

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
