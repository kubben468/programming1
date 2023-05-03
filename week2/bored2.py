"""
COMP.CS.100 Onko tylsää (virhetarkastelu)?.
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""
def main():

    read_words = True
    while read_words:

        word = str(input("Answer Y or N: "))
        if word == 'Y' or word == 'y' or word == 'N' or word == 'n':

            read_words = False
            print("You answered", word)

        else:
            print("Incorrect entry.")
            read_words = True

if __name__ == "__main__":
    main()