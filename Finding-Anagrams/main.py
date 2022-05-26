# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    """
    Checks if the two arguments passed are anagrams
    Spaces are irrelevant in anagrams.
    Anagrams are also case-insensitive.
    """
    # [assignment] Add your code here
    # convert arguments to lower case
    word = word.lower(); anagram = anagram.lower()

    new_word = ''; new_anagram = ''

    # Remove spaces in case the arguments are sentences
    for char in word:
        if char != ' ':
            new_word += char

    for char in anagram:
        if char != ' ':
            new_anagram += char
    # Check if they have same length, return False if not
    if len(new_word) != len(new_anagram):
        return False

    # sort both word and anagram
    sorted_word = sorted(new_word)
    sorted_anagram = sorted(new_anagram)

    # check if the sorted values are same, return False if not
    if sorted_word != sorted_anagram:
        return False

    return True

# ==== Sample tests ====

# print(find_anagram("adultery", "true lady")) # True
# print(find_anagram("William Shakespeare", "I am a weakish speller")) # True
# print(find_anagram('oWl', 'low ')) # True
# print(find_anagram('games', 'names')) # False
