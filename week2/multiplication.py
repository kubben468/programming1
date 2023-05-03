"""
COMP.CS.100 
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    number = int(input("Choose a number: "))

    multiplier = 1
    while number < 100:
        print(f"{multiplier} * {number} = {multiplier*number}")
        multiplier += 1
if __name__ == "__main__":
    main()
