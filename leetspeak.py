replacements = {
    'A': '4',
    'E': '3',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'T': '7'
}

string_to_convert = input("Please enter a sentence. ")
converted_string = ""

for i in range(len(string_to_convert)):
    if string_to_convert[i].upper() in replacements:
        converted_string += replacements[string_to_convert[i].upper()]
    else:
        converted_string += string_to_convert[i]

print(converted_string)