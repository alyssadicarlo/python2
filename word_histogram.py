phrase = input("Please enter a sentence: ")
histogram = {}

words = phrase.split(" ")
for word in words:
    if word.lower() in histogram:
        histogram[word.lower()] = histogram[word.lower()] + 1
    else:
        histogram[word.lower()] = 1

print(histogram)