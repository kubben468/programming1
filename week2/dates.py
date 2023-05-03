"""
COMP.CS.100 
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    day = 1
    month = 1

    while day < 32 and month < 13:
        print(f"{day}.{month}.")
        day += 1

        if day == 32:
            day = 1
            month += 1

        elif month == 2 and day == 29:
            day = 1
            month += 1

        elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 31:
            day = 1
            month += 1

if __name__ == "__main__":
    main()