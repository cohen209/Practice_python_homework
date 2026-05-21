user_string = input("write string: ")

string_length = len(user_string)

if string_length < 4:
    print("too short")
elif string_length > 9:
    print("too long")
else:
    print("OK")