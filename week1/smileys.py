
def returnSmiley(feelScore):
    """function returns suitable smiley according to the mood of the user"""
    if(1 == feelScore):
        return "A suitable smiley would be :'("
    elif(2 <= feelScore < 4):
        return "A suitable smiley would be :-("
    elif(3 < feelScore < 8):
        return "A suitable smiley would be :-|"
    elif(8 <= feelScore < 10):
        return "A suitable smiley would be :-)"
    elif(feelScore == 10):
        return "A suitable smiley would be :-D"
    else:
        return "Bad input!"


def main():

    feel = int(input("How do you feel? (1-10) "))

    print(returnSmiley(feel))

if __name__ == "__main__":

    main()