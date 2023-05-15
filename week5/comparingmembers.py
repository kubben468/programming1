"""
COMP.CS.100 
Compare elements in list
"""

def are_all_members_same(a):
    """function to return true if all are same, and false if not"""
    i = 0
    while i < len(a):
        if(a[0] == a[i]):
            i+=1
        else: 
            return False
    return True

def main():

    array = [1, 1, 1, 1, 1]
    print(are_all_members_same(array))

if __name__ == "__main__":
    main()
