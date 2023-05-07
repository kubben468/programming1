"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""

def read_input(a):
    """checks input for as long as its grater that zero"""
    value = int(input(a))
    while value <= 0:
        value = int(input(a))
        
    return value

def print_box(w, h, m):
    """prints the box with three parametes"""
    for i in range(h):
        print(w*m)

def main():
    width = int(read_input("Enter the width of a frame: "))
    height = int(read_input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
