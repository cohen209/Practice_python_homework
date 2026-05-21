#שאלה 1
number = float(input("write number: "))

if number >= 0:
    print("the number is positive")
else:
    print("the number is negative")

#שאלה 2
user_string = input("write string: ")

if len(user_string) > 0 and user_string[0] == 'A':

    modified_string = 'a' + user_string[1:]
    print("updated string :", modified_string)
else:
    print("the first character is not 'A' or the string is empty.")

    # שאלה 3
email = input("write email: ")

if len(email) < 4 or email[0] == '@' or email[-1] == '@':
    print("ERROR")
else:
    print(email + " is valid!")