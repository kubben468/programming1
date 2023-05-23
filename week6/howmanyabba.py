"""
COMP.CS.100 Programming 1
How many abbas?
"""

def count_abbas(a):
    """calculates how many abbas are in input"""
    counter = 0
    i = 0
    
    while i < len(a) - 3:
        if a[i:i+4] == "abba":
            counter += 1
            i += 1
        else:
            i += 1
    
    return counter
    
def main():
    
    print(count_abbas("abbabbabba"))
    
if __name__ == "__main__":
    main()