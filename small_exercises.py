list_of_numbers = [5,6,32,92,5,37,-10,34,-59,-29,4,-88]

# Number 1 - Sum the numbers
sum = 0
for number in list_of_numbers:
    sum = sum + number
print("Number 1: " + str(sum))

# Number 2 - Largest Number
largest = -1e9
for number in list_of_numbers:
    if number > largest:
        largest = number
print("Number 2: " + str(largest))

# Number 3 - Smallest Number
smallest = 1e9
for number in list_of_numbers:
    if number < smallest:
        smallest = number
print("Number 3: " + str(smallest))

# Number 4 - Even Numbers
print("Number 4: ")
for number in list_of_numbers:
    if number % 2 == 0:
        print(number)

# Number 5 - Positive Numbers
print("Number 5: ")
for number in list_of_numbers:
    if number > 0:
        print(number)

# Number 6 - Positive Numbers II
positive = []
for number in list_of_numbers:
    if number > 0:
        positive.append(number)
print("Number 6: " + str(positive))

# Number 7 - Multiply List
factor = 2
multiplied_by_factor = []
for number in list_of_numbers:
    multiplied_by_factor.append(number * factor)
print("Number 7: " + str(multiplied_by_factor))