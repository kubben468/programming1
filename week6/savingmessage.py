"""
COMP.CS.100 Programming 1
Code Template
"""

def read_message():
    """lukee viestin ja muuttaa sen isoiksi kirjaimiksi"""
    message = []
    text = input()

    while len(text) !=  0:
        message.append(text)
        text = input()

        if len(text) == 0:
            return message

def main():

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    index = 0
    print("The same, shouting:")

    while index < len(msg):
        row = msg[index]
        row = row.upper()
        print(row)
        index +=  1

if __name__ == "__main__":
    main()