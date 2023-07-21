import os
from Password_class import PasswordGenerator


def main():
    passwd = PasswordGenerator()
    atributes = ""
    while atributes != 6:
        os.system('cls')
        print("""
Hello, it is a  Password Generator!
You can choose which options you want to exclude from your password
By the defaults, your password contains 8 characters with at least 
one uppercase and one lowercase letters one digit and one special character     
""")

        print("""Options you may want to exclude or change: 
        1) Number
        2) Uppercase letters
        3) Uppercase letters
        4) Special characters
        5) Change length of password
        6) Generate password    
        """)

        atributes = input("Choose any option ")
        atributes_list = {"1": "include_digits",
                          "2": "include_uppercase",
                          "3": "include_lowercase",
                          "4": "include_special_chars"
                          }
        if atributes in atributes_list:
            setattr(passwd, atributes_list[atributes], False)
        elif atributes == "5":
            print(passwd.length_input())
            input("Enter to continue ")
        elif atributes == "6":
            print(passwd.generate_password())
            exit(0)
        else:
            print("Options does`nt exist")
            input("Enter to continue ")


if __name__ == "__main__":
    main()
