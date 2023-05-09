"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""

from math import pi

def squareCalculations(side):
    """function to calculate circumference and area for square"""
    c = 4*side
    a = side**2
    printCircumference(c)
    printSurfaceArea(a)
    
def rectangleCalculations(side1, side2):
    """function to calculate circumference and area for rectangle"""
    c = 2*side1 + 2*side2
    a = side1 * side2
    printCircumference(c)
    printSurfaceArea(a)
    
def circleCalculations(radius):
    """function to calculate circumference and area for circle"""
    c = 2 * pi * radius
    a = pi * radius**2
    printCircumference(c)
    printSurfaceArea(a)
    
def readInput(i):
    """returns input if it larger than 0"""
    answer = float(input(i))
    while answer <= 0:
        answer = float(input(i))
    return answer

def printCircumference(c):
    """prints circumfrence of a given shape"""
    print(f"The circumference is {c:.2f}")
    
def printSurfaceArea(a):
    """prints surface area of a given shape"""
    print(f"The surface area is {a:.2f}")

def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            side = readInput("Enter the length of the square's side: ")
            squareCalculations(side)
            
            pass

        elif answer == "r":
            side1 = readInput("Enter the length of the rectangle's side 1: ")
            side2 = readInput("Enter the length of the rectangle's side 2: ")
            rectangleCalculations(side1, side2)
            
            pass
        
        elif answer == "c":
            radius = readInput("Enter the circle's radius: ")
            circleCalculations(radius)
            
            pass

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")
            
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
