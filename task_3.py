import re


# USERNAME VALIDATION
username = input("""\nusername
username should have atleast one '.' and '_'
and should atleast be 8 in length.\n
Enter your username : """)
user_pattern = r"^(?=.*\.)(?=.*_).{8,}$"
match_user = re.search(user_pattern, username)

if "_" not in username and "." not in username:
    print("username should have atleast one '.' and '_'")
    
if len(username) < 8:
    print("Error: username should be atleast 8 in length")

# PASSWORD VALIDATION
password = input("""\npassword
Atleast one of the following '@,#,$,%'.
Atleast one uppercase letter and lowercase letter
Atleast one digit from 0-9.\n
Enter your password : """)
pass_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#\$%]).*$" 
match_pass = re.search(pass_pattern, password)

def check_password(password):
    special_chars = "@#$%"
    has_upper = False
    has_lower = False
    if not any(char in special_chars for char in password):
        print("Error: Password must contain at least one of the following special characters: @ # $ %")
    
    if len(password) < 8:
        print("Error: username should be atleast 8 in length")
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
    if not has_upper:
        print("Error: Password must contain uppercase letters.")
    elif not has_lower:
        print("Error: Password must contain lowercase letters.")
    
    return True

# FUNCTION CALL
check_password(password)
