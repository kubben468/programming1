def calculateChange(price, amount):
    """function returns amount of different change"""
    change = amount - price

    if change <= 0:
        print("No change")
    else:
        print("Offer change:")
        tens = change // 10
        if tens != 0:
            print(f"{tens} ten-euro notes")
        tensOver = change % 10
        
        fives = tensOver // 5
        if fives != 0:
            print(f"{fives} five-euro notes")
        fivesOver = tensOver % 5

        twos = fivesOver // 2
        if twos != 0:
            print(f"{twos} two-euro coins")
        twosOver = fivesOver % 2
        
        ones = twosOver // 1
        if ones != 0:
            print(f"{ones} one-euro coins")

def main():

    price = int(input("Purchase price: "))
    amount = int(input("Paid amount of money: "))

    calculateChange(price, amount)

if __name__ == "__main__":

    main()