"""
COMP.CS.100 Programming 1
ROT13 program code template
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

def main():
    
    print(row_encryption("Happy, happy, joy, joy!"))

if __name__ == "__main__":
    main()