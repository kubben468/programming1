"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name:
Email:
"""

def main():
    
    row = 1
    filename = input("Enter the name of the file: ")
    
    file = open(filename, mode="r")

    for line in file:
        output = (f"{row} {line.rstrip()}")
        print(output)
        row += 1
    
    file.close()

if __name__ == "__main__":
    main()
