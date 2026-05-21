#שאלה 1 
age = int(input("write age: "))

if age < 0:
    age = 0
elif age > 120:
    age = 120

if 0 <= age <= 18:
    print("teenager")
else:
    print("adult")

    #שאלה 2
password = input("write password: ")

is_valid = True

if len(password) < 8:
    print("the password must be at least 8 characters long.")
    is_valid = False

if len(password) > 0 and password[0] != 'Z' and password[0] != 'C':
    print("the password is not valid: the first character must be Z or C.")
    is_valid = False

if len(password) > 0 and password[-1] != '$':
    print("the password is not valid: the password must end with '$'.")
    is_valid = False

if is_valid:
    print("STRONG PASSWORD")