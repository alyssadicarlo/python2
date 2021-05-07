list_of_numbers = [2,5,2,12,4,2,1,5,8,6,5,6,6]
no_duplicates = []

for num in list_of_numbers:
    if num not in no_duplicates:
        no_duplicates.append(num)

print(no_duplicates)