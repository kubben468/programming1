"""
COMP.CS.100 
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    choice = int(input("How many numbers would you like to have? "))
    repetition = 0
    number = 1
    while repetition < choice:

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
