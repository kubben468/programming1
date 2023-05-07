"""
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(a, b, c):
    """calucates area of triange when length of three sides are provided"""
    s = (a + b + c)/2
    A = sqrt((s*(s-a))*(s-b)*(s-c))
    return A

def main():
    line1 = float(input("Enter the length of the first side: "))
    line2 = float(input("Enter the length of the second side: "))
    line3 = float(input("Enter the length of the third side: "))

    print(f"The triangle's area is {area(line1, line2, line3):.1f}")


if __name__ == "__main__":
    main()
