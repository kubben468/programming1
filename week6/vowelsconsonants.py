"""
COMP.CS.100 Programming 1
Vowels and Consonants
"""

def main():
    word = input("Enter a word: ")
    vowels = "aeiouy"
    
    vowel = 0
    consonant = 0
    
    for i in word:
        if i in vowels:
            vowel += 1
        else:
            consonant += 1
    print(f'The word "{word}" contains {vowel} vowels and {consonant} consonants.')
    
if __name__ == "__main__":
    main()