"""
COMP.CS.100 
Number sequence
"""

def main():
    print("Give 5 numbers:")
    list = []
    for i in range(5):
        element = int(input("Next number: ")) 
        list.append(element)
    
    print("The numbers you entered that were greater than zero were:")
    for element in list:
        if element > 0:
            print(element)
     
if __name__ == "__main__":
    main()