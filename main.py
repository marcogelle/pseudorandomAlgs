# import sys
import lcg

if __name__ == '__main__':
    prng = lcg.LinearCongruential()
    print("Welcome this pseudorandom number generator!")
    print("Enter n to generate a number")
    print("Type exit to exit this program")
    while True:
        command = input("Command: ")
        if command == 'n':
            print(prng.generate())
        elif command == 'exit':
            break
        else:
            print('Invalid command')
