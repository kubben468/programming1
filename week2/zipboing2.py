"""
COMP.CS.100 
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    choice = int(input("How many numbers would you like to have? "))
    repetition = 1
    number = 1
    for number in range(repetition, choice + 1):

        if number % 7 == 0 and number % 3 == 0:
            print("zip boing")
        
        elif number % 7 == 0:
            print("boing")
        
        elif number % 3 == 0:
            print("zip")

        else:
            print(number)

        number += 1
        repetition += 1

    
if __name__ == "__main__":
    main()
