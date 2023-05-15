"""
COMP.CS.100 
List as return
"""

def input_to_list(n):
    """
    Asks the user to enter n integers and returns them as a list.
    """
    numbers = []
    for i in range(n):
        num = int(input())
        numbers.append(num)
    return numbers


def main():
    # Get the number of integers to be processed
    n = int(input("How many numbers do you want to process: "))
    print(f"Enter {n} numbers:")

    # Read the numbers from the user
    numbers = input_to_list(n)

    # Search for a number
    search_num = int(input("Enter the number to be searched: "))
    count = numbers.count(search_num)

    # Print the result
    if count == 0:
        print(f"{search_num} is not among the numbers you have entered.")
    else:
        print(f"{search_num} shows up {count} times among the numbers you have entered.")


if __name__ == "__main__":
    main()
