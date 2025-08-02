# min. be 8 characters
# at least uppercase
# at least lowercase
# at least one number
# at least one special character

import random
import string
import pyperclip

#function to generate secure passwords
def generate_password(length=8):
    #enforce minimum length
    if length < 8:
        raise ValueError("length of the password must contain at least 8 characters.")

    #ensure all the requirements for generating a password is met
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

    #pool of all valid characters for remaining positions
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    remaining = [random.choice(all_chars) for _ in range(length - 4)]
    
    #combine all characters and shuffle to randomize order
    password_list = list(lower + upper + digit + special + ''.join(remaining))
    random.shuffle(password_list)

    return ''.join(password_list)

#main program to interact with the user in the console
print("welcome to the password generator !")
try:
    num_passwords = int(input("how many passwords do you want to generate? "))
    length = int(input("enter desired password length (min. 8): "))
    copy_option = input("do you want to copy the last password to clipboard? (yes/no): ").strip().lower()

    if length < 8:
        print("length of the password must contain at least 8 characters.")
    else:
        for i in range(num_passwords):
            pw = generate_password(length)
            print(f"password {i+1}: {pw}")
        
        if copy_option == "yes":
            pyperclip.copy(pw)
            print("!! last password is copied to clipboard !!")

except ValueError:
    print("please enter valid numbers.")
except Exception as e:
    print(f"ERROR: {e}")