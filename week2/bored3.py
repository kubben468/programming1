"""
COMP.CS.100 
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    read_words = True

    while read_words:
        word = input("Bored? (y/n) ")

        if word == 'y' or word == 'Y':
            read_words = False
            print("Well, let's stop this, then.")

        elif word == 'N' or word == 'n':
            read_words = True

        else:
            print("Incorrect entry.")
            read_words = True

if __name__ == "__main__":
    main()