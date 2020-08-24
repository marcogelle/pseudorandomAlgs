import lcg

if __name__ == '__main__':
    prng = lcg.LinearCongruential()
    print("Welcome this pseudorandom number generator!")
    print("Enter n to generate a number")
    print("Enter s to display the current seed of your PRNG")
    print("Type exit to exit this program")
    print()

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
