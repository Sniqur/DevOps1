import string
import random

print("Welcome to the Linux User Password Generator!\n")
#input the length of your password
try:
    passwordLength = int(input("""
Please enter the desired password length:
(Enter the number between 4 - 50): """))
    print()

    if passwordLength < 4 or passwordLength > 50:
        print("The number must be between 4 - 50 : ")
        exit()

except:
    print("Something went wrong! You can enter only numbers!")
    exit()

#using random letters, digits and signs for a password

symbols = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all = symbols + digits + punctuation

#randomly create the password

randomPass = random.sample(all, passwordLength)

password = "".join(randomPass)

print(password)