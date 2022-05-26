"""
This is a program to count the number of words in a given text

"""

def count_words(text):
	"""counts words in text"""
	count = 0
	list_of_words = text.split()

	for word in list_of_words:
		count += 1

	return count

text = "I love to code but I sometimes fail, failure is not when I miss it but when I refuse to get up and try again, albeit, learning from the miss!"

print("Number of words in the text is {}".format(count_words(text)))
