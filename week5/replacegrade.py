"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

def convert_grades(a):
    """function replace list value if value is not equal to 0"""
    i = 0
    while i < len(a):
        if a[i] != 0:
            a[i] = 6
        i += 1
    return a


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
