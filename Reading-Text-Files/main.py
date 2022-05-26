# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        content = f.read()

    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '] # add space to the list for splitting
    text = text.lower()

    new_text = ''
    counted = {}

    for char in text:
        if char in alpha:
            new_text += char

    words = new_text.split()

    for word in words:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1

    return counted

# print(count_words())
