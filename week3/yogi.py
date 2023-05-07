"""
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""

def repeat_name(name, amount):
    """function to print line specific amount of times"""
    if amount == 1:
        print(f"{name}, {name}")
    elif amount == 3:
        for i in range(amount):
            print(f"{name}, {name} Bear")
    else:
        print(f"{name}, {name} Bear")
        
def verse(lyrics, name):
    """structure of the song"""
    print(lyrics)
    repeat_name(name, 1)
    print(lyrics)
    repeat_name(name, 3)
    print(lyrics)
    repeat_name(name, 2)

    
def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
