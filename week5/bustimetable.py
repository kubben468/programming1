"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

def checkNextBusses(a, c):
    """function to return index of element in list that is greater than c"""
    next = 0
    for i in range(len(a)):
        if a[i] >= c:
            next = i
            break
    return next
        
def main():
    
    timetable = [630, 1015, 1415, 1620, 1720, 2000]
    currentTime = int(input("Enter the time (as an integer): "))
    
    i = checkNextBusses(timetable, currentTime)
    print("The next buses leave:")
    for i in range(i, i+3):
        print(timetable[i % len(timetable)])

if __name__ == "__main__":
    main()
