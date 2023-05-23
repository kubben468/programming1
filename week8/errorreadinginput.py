"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:

Template for sorting by price assignment.
"""

def print_box(w, h, m):
    """prints bow with given specs"""
    for i in range(h):
        print(w*m)
        i += 1
        
def read_input(a):
    """checks if input is valid or not"""
    value = input(a)
    invalid_input = True
    while invalid_input:
        try:
            value = input(a)
            value = int(value)
            if value >= 0:
                invalid_input = False

        except ValueError:
            invalid_input = True
    while value <= 0:
        value = int(input(a))
    return value
    
def main():
    
    width = read_input("Enter the width of a frame: ")
    heigth = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, heigth, mark)
    

if __name__ == "__main__":
    main()
