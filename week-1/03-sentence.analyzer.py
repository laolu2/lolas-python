# Asks the user to input a sentence.
# Performs the following operations:
# 1. Counts the total number of words in the sentence (split by spaces).
# 2. Converts the sentence to uppercase and prints it.
# 3. Reverses the sentence and prints it.

sentence = input("Enter a sentence: ")

words = sentence.split(" ")
num_words = len(words)

characters = list(sentence)
reversed_characters = reversed(characters)
reversed_sentence = "".join(reversed_characters)

print(f"Number of Words is {num_words}")
print(f"Sentence in Upper is {sentence.upper()}")
print(f"Reversed: {reversed_sentence}")