"""
COMP.CS.100 
Going through the list indices
"""

def main():
    print("Give 5 numbers:")
    list = []
    for i in range(5):
        element = int(input("Next number: ")) 
        list.append(element)
    
    print("The numbers you entered, in reverse order:")
    for i in reversed(list):
        print(i)
     
if __name__ == "__main__":
    main()