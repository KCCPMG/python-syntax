"""
For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
"""
words = ["hello", "hey", "goodbye", "yo", "yes"]
for word in words:
  print(word.upper())


def print_upper_words(word_arr):
  """
  Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)
  """
  for word in word_arr:
    print(word.upper())

print("\nTesting print_upper_words (v1)")
print_upper_words(words)


def print_upper_words(word_arr):
  """
  Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
  """
  for word in word_arr:
    if word[0] == "e" or word[0] == "E":
      print(word.upper())

print("\nTesting print_upper_words (v2)")
print_upper_words(["ello", "ey", "yo", "yes"])


def print_upper_words(word_arr, letter_arr):
  """
  Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
  """
  upper_letter_arr = []
  for letter in letter_arr:
    upper_letter_arr.append(letter.upper())

  for word in word_arr:
    if upper_letter_arr.count(word[0].upper()) > 0:
      print(word.upper())


  




print("\nTesting print_upper_words (v3)")
print_upper_words(["hello", "hey", "yo", "yes", "Thanksgiving"], ["H","t", "l"])