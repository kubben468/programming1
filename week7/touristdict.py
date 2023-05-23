"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {"hola": "hey", "gracias": "thanks", "casa": "home"}
    print("Dictionary contents:")
    dictionary = ", ".join(sorted(english_spanish))
    print(dictionary)
    
    while True:
        
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            wordToTranslate = input("Enter the word to be translated: ")
            if wordToTranslate in english_spanish:
                print(f"{wordToTranslate} in Spanish is {english_spanish[wordToTranslate]}")
            else:
                print(f"The word", wordToTranslate, "could not be found from the dictionary.")

        elif command == "A":
            english = input("Give the word to be added in English: ")
            spanish = input("Give the word to be added in Spanish: ")
            english_spanish[english] = spanish
            spanish_english[spanish]= english
            print("Dictionary contents:")
            dictionary = ", ".join(sorted(english_spanish))
            print(dictionary)

        elif command == "R":
            wordToRemove = input("Give the word to be removed: ")
            if wordToRemove in english_spanish:
                del english_spanish[wordToRemove]
            if wordToRemove in spanish_english:
                del spanish_english[wordToRemove]
            else:
                print(f"The word {wordToRemove} could not be found from the dictionary.")
            
        elif command == "P":
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")
            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(f"{word} {spanish_english[word]}")
            print()
                
        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            text = text.split(" ")
            index = 0
            print("The text, translated by the dictionary:")

            wordlist = []

            while index < len(text):

                if text[index] in english_spanish:
                    translated_word = english_spanish[text[index]]
                    wordlist.append(translated_word)
                    index += 1

                else:
                    translated_word = text[index]
                    wordlist.append(translated_word)
                    index += 1

            translation = " ".join(wordlist)
            print(translation)
            
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
