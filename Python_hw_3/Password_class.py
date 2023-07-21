import string
import random


class PasswordGenerator:

    def __init__(self):
        self.length = 8
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_digits = True
        self.include_special_chars = True

    def rand_characters(self):
        random_ls = []
        if self.include_digits == True:
            random_ls.append(random.choice(string.digits))
        if self.include_uppercase == True:
            random_ls.append(random.choice(string.ascii_uppercase))
        if self.include_lowercase == True:
            random_ls.append(random.choice(string.ascii_lowercase))
        if self.include_special_chars == True:
            random_ls.append(random.choice(string.punctuation))
        try:
            return random.choice(random_ls)
        except:
            print("Something went wrong")
            exit(0)

    def password_generate(self):
        password = " "
        for i in range(self.length):
            password = password + self.rand_characters()
        return print("your password is ", {password})

    def length_input(self):
        try:
            self.length = int(input("Entet the length of your password (8 - 256 digits): "))
        except ValueError:
            print("Length has been changed to defaults (8 digits)", {self.length})

        self.check_length()

    def check_length(self):
        if self.length < 8 or self.length > 256:
            self.length = 8
            print("Length does not match to requirements")
