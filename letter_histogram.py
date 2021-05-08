word = input("Please enter a word: ")
histogram = {}

for letter in word:
    if letter in histogram:
        histogram[letter] = histogram[letter] + 1
    else:
        histogram[letter] = 1
print(histogram)