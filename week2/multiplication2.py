"""
COMP.CS.100 
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    number = int(input("Choose a number: "))
    output = 0
    multiplier = 1
    while output < 100:
        output = number * multiplier
        print(f"{multiplier} * {number} = {output}")
        multiplier += 1
if __name__ == "__main__":
    main()
