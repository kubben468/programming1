"""
COMP.CS.100 Programming 1
Longest substring
"""
   
def longest_substring_in_order(string):
    """function to count longest substring in order"""
    if len(string) <= 1:
        return string

    longest_substring = string[0]
    current_substring = string[0]

    for i in range(1, len(string)):
        if string[i] >= string[i-1]:
            current_substring += string[i]
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = string[i]

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring
    
def main():
    
    print(longest_substring_in_order("abcabcdefgabab"))  # Output: 'abcdefg'

    
if __name__ == "__main__":
    main()