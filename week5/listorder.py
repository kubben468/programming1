"""
COMP.CS.100 
Check if list is in order
"""

def is_the_list_in_order(a):
    """function to return true if elements are in order"""
    i = 0
    while i < len(a)-1:
        if(a[i] <= a[i+1]):
            i+=1
        else: 
            return False
    return True

def main():

    array = [1, 2, 6, 6, 8, 9]
    print(is_the_list_in_order(array))

if __name__ == "__main__":
    main()
