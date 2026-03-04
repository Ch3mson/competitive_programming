"""
We're interested in knowing how often different word lengths appear in English text. The goal of this exercise is to print a histogram to stdout, where each bar represents the frequency of a given word length. The output is normalized so that the largest histogram bar is always 10 characters -- this guarantees that it's easy to read.

Here's example output from processing the sentence "Hi there - my first name is Max"

```
#  
#
#
#     #
#     #
#     #
#     #
# # # #
# # # #
# # # #
2 3 4 5

# Assumptions
Always round to nearest integer for pound display
```

The math to figure out the size of a given bar is `round((frequency / max_frequency) * 10)`

Let's assume that any non-alphabetic character should be removed. To validate words, lets use the /usr/share/dict/words file as a source of correctly spelled words. It comes standard with most unix systems. If using Codesignal, you can install it using these commands in the terminal:

```
$ apt-get update
$ apt-get install --reinstall wamerican
```

Let's get the provided example working first and then try running the program using a larger data set: https://www.gutenberg.org/files/84/84-0.txt. We'll pull it using a network request within the code of your solution.
"""

# if frequencies are non-zero but the bar length is zero, then do we want to omit it from the histogram? (yes)
# if words have hyphens? do we omit them? (i.e. co-op => coop)
# ignoring punctuation and any non alphabetical characters?
# case sensitivity? (yes)
# if a word is valid but isn't in the words file, we still not consider it a word? (yes)

# cases
# valid word, but not in the words file 
# process words with special characters (get rid of them)
# handle case sensitivity with words
# omit non-zero frequencies that round down to bar length of zero
# ignore punctuation 

# data members 
# word length frequency hash
# key: word length (int)
# value: frequency (int)

# max bar length
# max word length

# 1. fetch all the words from the file, conver tthem into lower case (to handle case sensitivity) and then add them to a set 
#    less complex to check the existence of words (o(1) vs. o(n))

# 2. create a class that is initialized with a string (first, we will pass in the example)
# 3. split into an array of words (by any type of whitespaces, newlines, etc. )
# 4. iterate through the word & update them to exclude any non-alpha characters 
# 5. 	check if this word exists in the word list. if it does, increment the frequency of this updated length by 1
# 6. after iterating through all the words, update the values in the hash to its bar length using `round((frequency / max_frequency) * 10)`
#    if the bar length is zero, pop it from the hash
#    also update the highest bar length 
# 7. print the histogram 
#    start from the top-most bar length and go down one level at a time until 1 
#    iterate through the range of word lengths [1, max word length]
#    if the word length is not in the frequency hash (or its value is 0), then continue
#    otherwise, if the bar length is >= the current level, we will print "#" and " " if not 
#    to keep the format consistent, i will use an array to store these values 
# 8. print each array one at a time to produce the histogram 
# 9. print the keys in that exist in the hash in incrementing order

from collections import defaultdict
from http import HTTPStatus

import requests

_MIN_WORD_LENGTH = 1

class HistogramApp:
	def __init__(self, string: str) -> None:
		self.input_words = string.split()
		self.bar_lengths = defaultdict(int)
		self.dict_url = "/usr/share/dict/words"
		self.valid_words = set()

		self.max_bar_length = 0
		self.max_word_length = 0
		self.max_word_freq = 0
	
	def update_valid_words(self):
		with open(self.dict_url, 'r') as f:
			file_content = f.readlines()

			for line in file_content:
				self.valid_words.add(line.strip().lower())
	
	def process_input_string(self):
		for word in self.input_words:
			updated_word = self.update_word(word.lower())
			
			if updated_word not in self.valid_words:
				continue
			
			self.bar_lengths[len(updated_word)] += 1
			self.max_word_freq = max(self.max_word_freq, self.bar_lengths[len(updated_word)])
			self.max_word_length = max(self.max_word_length, len(updated_word))
	
	def update_bar_lengths(self):
		for word_len, freq in self.bar_lengths.items():
			self.bar_lengths[word_len] = round((freq / self.max_word_freq) * 10)
			self.max_bar_length = max(self.bar_lengths[word_len], self.max_bar_length)
		
	def print_histogram(self):
		for level in range(self.max_bar_length, 0, -1):
			histogram_level = []

			for word_len in range(_MIN_WORD_LENGTH, self.max_word_length + 1):
				if not self.bar_lengths[word_len]:
					continue 

				histogram_level.append("#" if self.bar_lengths[word_len] >= level else " ")
			
			print(" ".join(histogram_level))
		
		histogram_buckets = [str(word_len) for word_len in range(_MIN_WORD_LENGTH, self.max_word_length + 1) if self.bar_lengths[word_len]]
		print(" ".join(histogram_buckets))
	
	def update_word(self, word: str):
		return "".join([c for c in word if c.isalpha()])

def main():
	text_url = "https://www.gutenberg.org/files/84/84-0.txt"

	response = requests.get(text_url)

	if response.status_code == HTTPStatus.OK:
		text = response.text

	app = HistogramApp(text or "Hi there - my first name is Max")
	app.update_valid_words()
	app.process_input_string()
	app.update_bar_lengths()
	app.print_histogram()

if __name__ == "__main__":
	main()
