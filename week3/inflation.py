"""
COMP.CS.100 Project: Inflation Calculator
Creator: Aukusti Leipälä
StudentNumber: 050087329
'Program' to calculate max difference of inflation rate from user inputs
"""

def calculateDifference(current, previous):
    """calculates difference between current and previous month infaltionrate"""
    difference = current - previous
    return difference

def finalPrint(a):
    """function is responsible for final print"""
    if len(a) < 1:
        print("Error: at least 2 monthly inflation rates must be entered.")
    else:
        maxDifference = max(a)
        print(f"Maximum inflation rate change was {maxDifference:.1f} points.")

def main():
    """asks user for inflation rate of a month and calculates the difference"""
    previousRate = None
    # list of all the differences between months inflation rates
    largestDifference = []
    monthCounter = 1

    while True:
        answer = input(f"Enter inflation rate for month {monthCounter}: ")
        monthCounter += 1
        # checks whether answer is empty or not
        if answer == "":
            break
        currentRate = float(answer)
        # if answer is not empty calls for function to calculate the difference
        if previousRate is not None:
            largestDifference.append(calculateDifference(currentRate, previousRate))

        previousRate = currentRate
        
    finalPrint(largestDifference)

if __name__ == "__main__":
    main()


