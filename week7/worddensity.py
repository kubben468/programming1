"""
COMP.CS.100 Programming 1
Word density counter
"""

def main():

    SANAT = {}

    print("Enter rows of text for word counting. Empty row to quit.")
    lause = "a"

    while len(lause.strip()) > 0:
        lause = input().lower()
        sana = lause.split(" ")
        index = 0

        while index < len(sana):
            if sana[index] not in SANAT:
                SANAT[sana[index]] = 1
                index += 1

            else:
                SANAT[sana[index]] += 1
                index += 1

    for word in sorted(SANAT):
        if len(word) > 0:
            print(f"{word} : {SANAT[word]} times")

if __name__ == "__main__":
    main()