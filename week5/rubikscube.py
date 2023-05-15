"""
COMP.CS.100 
Calculates averagetime time for solving rubik's cube
"""

def calculate_average(a):
    """function to return true if elements are in order"""
    a.remove(max(a))
    a.remove(min(a))
    i = 0
    total = 0
    while i < len(a):
        total += a[i]
        i+=1
    average = total/len(a)
    return average

def main():

    array = []
    repetition = 1
    while repetition < 6:
        time = float(input(f"Enter the time for performance {repetition}: "))
        array.append(time)
        repetition += 1
    print(f"The official competition score is {calculate_average(array):.2f} seconds.")
    

if __name__ == "__main__":
    main()
