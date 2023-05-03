"""
COMP.CS.100 Fibonaccin lukusarja.
Tekijä: Aukusti Leipälä
Opiskelijanumero: 050087329
"""

def main():

    count = int(input("How many Fibonacci numbers do you want? "))
    old_num = 1
    prev_num = 0
    reps = 0
    wanted_reps = count - 1
    order = 2

    if count == 0:
        print("")

    elif count == 1:
        print("1. 1")

    else:
        print("1. 1")
        while reps < wanted_reps:

            new_num = old_num + prev_num

            print(f"{order}. {new_num}")
            prev_num = old_num
            old_num = new_num
            order += 1
            reps += 1

if __name__ == "__main__":

    main()