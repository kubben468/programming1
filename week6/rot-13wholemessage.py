"""
COMP.CS.100 Programming 1
"""

def encrypt(text):

    """
    Encrypts its parameter using ROT13 encryption technology.
    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    if text == "":
        return text

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    caps = text.isupper()
    text = text.lower()

    if text not in regular_chars:
        return text
    index = 0

    while index < len(regular_chars):
        if regular_chars[index] == text:
            if caps == True:
                return encrypted_chars[index].upper()
            else:
                return encrypted_chars[index]
        index += 1

def row_encryption(text):
    """salaa lauseen tai useita kirjaimia"""

    index = 0
    encrypted_text = ""

    while index < len(text):
        encrypted_letter = encrypt(text[index])
        encrypted_text += encrypted_letter
        index += 1

    return encrypted_text

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
    print("ROT13:")

    while index < len(msg):
        row = row_encryption(msg[index])
        print(row)
        index +=  1

if __name__ == "__main__":
    main()