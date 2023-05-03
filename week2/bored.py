"""
COMP.CS.100 Ohjelmointi 1.
Program about while loop and to check if user is bored
"""

def main():

    runProgram = True
    
    while runProgram:
        answer = input("Bored? (y/n) ")

        if answer == "y":
            runProgram = False
            print("Well, let's stop this, then.")
    

if __name__ == "__main__":
    main()