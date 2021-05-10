print("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")

running = True
phonebook = {}

while running == True:
    
    # Handlie invalid input
    try:
        user_input = int(input("What do you want to do (1-5)? "))
    except:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    # Look up entry in phonebook
    if user_input == 1:
        name = input("Name: ")
        names_found = []
        if name in phonebook:
            names_found.append(name)
            print("Found entry for %s: %s" % (name, phonebook[name]["phone_number"]))
        if names_found == []:
            print("No entries found.")
    
    # Add entry to phonebook
    elif user_input == 2:
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        phonebook[name] = {
            "phone_number": phone_number
        }
        print("Entry stored for %s." % (name))
    
    # Delete an entry from phonebook
    elif user_input == 3:
        name = input("Name: ")
        if name in phonebook:
            del phonebook[name]
        print("Deleted entry for %s." % (name))
    
    # List all entries
    elif user_input == 4:
        for entry in phonebook:
            print("Found entry for %s: %s" % (entry, phonebook[entry]["phone_number"]))
    # Quit
    elif user_input == 5:
        running = False
        
    # Handle invalid input
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
