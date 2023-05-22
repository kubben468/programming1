"""
COMP.CS.100 Programming 1
Aukusti Leipälä
050087329, aukusti.leipala@tuni.fi
Project that calculates changes in seawater. User can give seawater level
as an input and program will return different values form them such as
maximum and minimum level, meadian and mean values and deviation.
"""

from math import sqrt

LIST_LENGTH_ERROR = "Error: At least two measurements must be entered!"

def mimimum(a):
    """determines max value of list
    Args:
        a (list): list of user inputs

    Returns:
       float: min value of list
    """
    return min(a)

def maximum(a):
    """determines min value of list

    Args:
        a (list): list of user inputs

    Returns:
        float: max value of list
    """
    return max(a)
    
def median(a):
    """determines median value of list

    Args:
        a (list): list of user inputs

    Returns:
        float: median value of list
    """
    list = sorted(a)
    l = int(len(a))
    
    # if length of list is even number
    if len(a) % 2 == 0:
        medianValue = ((list[int(l/2)]) + (list[int((l/2)) - 1])) / 2
    # else length of list is odd number
    else:
        medianValue = list[int((l/2))]
    return medianValue

def mean(a):
    """determines mean value of list
    
    Args:
        a (list): list of user inputs
    Returns:
        float: mean value of list
    """
    total = 0.0
    i = 0
    # for loop to go through all elements and to add 
    # them into variable
    for i in range(len(a)):
        total += a[i]
    
    return total/len(a)

def deviation(a):
    """determines deviation value of list

    Args:
        a (list): list of user inputs

    Returns:
        float: return standard deviation of list
    """
    l = int(len(a))
    meanValue = mean(a)
    sum = 0.0
    # for loop to go through elements in list and to add 
    # them into variable
    for i in range(len(a)):
        sum += ((a[i] - meanValue)**2)
    
    deviationValue = sqrt((1/(l-1))*sum)
    
    return deviationValue

def checkListLength(a):
    """checks if length of list correct

    Args:
        a (list): list of user inputs
    """
    if len(a) < 2:
        print(LIST_LENGTH_ERROR) 

    else:
        printResult(a) 

def printResult(a):
    """prints results in correct format

    Args:
        a (list): list of user inputs
    """
    
    print("{:<10} {:.2f} cm".format("Minimum:", mimimum(a)))
    print("{:<10} {:.2f} cm".format("Maximum:", maximum(a)))
    print("{:<10} {:.2f} cm".format("Median:", median(a)))
    print("{:<10} {:.2f} cm".format("Mean:", mean(a)))
    print("{:<10} {:.2f} cm".format("Deviation:", deviation(a)))

def main():
    
    levels = []
    print("Enter seawater levels in centimeters one per line.\nEnd by entering an empty line.")    
    while True:
        level = input()
        
        if level == "":
            break
        
        else:
            levelInput = float(level)
            levels.append(levelInput)
    
    checkListLength(levels)
    

if __name__ == "__main__":
    main()