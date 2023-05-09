"""
COMP.CS.100 
Comparing floating-point (decimal) numbers
"""

def readInput(total, drawn):
    """reads user inputs and returns boolean"""
    if total <= 0 or drawn <= 0:
        print("The number of balls must be a positive number.")
        return False
    elif total < drawn:
        print("At most the total number of balls can be drawn.")
        return False
    else:
        return True
    

def factorial(a):
    """calulates factorial of a number"""
    number = a
    for i in range(1, number):
        number = number * i
    return number
    

def calculatePossibilites(total, drawn):
    """calculates number of possible combinations with given numbers"""
    result = factorial(total)/(factorial(total-drawn)*factorial(drawn))
    return result

def main():

    totalNumber = int(input("Enter the total number of lottery balls: "))
    drawnBalls = int(input("Enter the number of the drawn balls: "))
    if readInput(totalNumber, drawnBalls) == True:
        pos = calculatePossibilites(totalNumber, drawnBalls)
        print(f"The probability of guessing all {drawnBalls} balls correctly is 1/{pos:.0f}")
        
if __name__ == "__main__":
    main()