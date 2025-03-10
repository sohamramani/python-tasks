print("PHONE DIRECTORY")
# USER INPUT FUNCTION
def user_input():
    global user_selection 
    user_selection = int(input("""
    1 for add number
    2 for search contact using name or number. 
    3 for update speciﬁc contact details (name or number)
    0 for exit \n
    Select any one of the following : """))
    return user_selection

# FUNCTION CALL FOR DISPLAY
user_input()

# PHONE DIRECTORY
phone_directory = {}

while True:
    # ADD NUMBER TO DICTIONARY
    if user_selection == 1:
        try:
            name = str(input("Enter name: "))
            
            if name == "exit":
                print("you cannot set the name 'exit'")
                continue
            number = str(int(input("Enter number: ")))
            if 9 < len(number) < 11:
                phone_directory[name] = number
                print(phone_directory)
                print("name and number added successfully")
                user_input()
            else:
                print("Please enter a valid 10 digit number")
        except ValueError:
            print("Please enter a valid number")
    
    # SEARCH NUMBER 
    if user_selection == 2:
        try:
            search = str(input("Enter name or number to search ('exit' for stop): "))
            if search in phone_directory:
                print(f"Name: {search} \nNumber: {phone_directory[search]}")
            elif search:
                for key, val in phone_directory.items():
                    if val == search:
                        print(f"Name: {key} \nNumber: {search}")
                    else:
                        print("Contact not found")
            else:
                print("Contact not found")
            if search == "exit":
                user_input()
            
        except ValueError:
            print("Please enter a valid name or number")
    
    # UPDATE NUMBER WITH NAME OR NUMBER
    if user_selection == 3:
        update_the_value = input("""
            1 for update with name
            2 for update with number
            0 for exit
            Enter value :  """)
        if update_the_value == "1":
            name = input("Enter name to update: ")
            if name in phone_directory:
                new_name = input("Enter new name: ")
                if new_name == "exit":
                    print("you cannot set the name 'exit'")
                    continue
                phone_directory[new_name] = phone_directory.pop(name)
                print(phone_directory)
                print("name updated successfully")
                user_input()
            else:
                print("name not found")
        if update_the_value == "2":
            number = input("Enter number to update: ")
            if number in phone_directory.values():
                new_number = input("Enter new number: ")
                for key, val in phone_directory.items():
                    if val == number:
                        phone_directory[key] = new_number
                        print(phone_directory)
                        print("number updated successfully")
                        user_input()
            else:
                print("number not found")
        if update_the_value == "0":
            user_input()
    
    # EXITE THE PROGRAM
    if user_selection == 0:
        print("Exiting the program")
        break
