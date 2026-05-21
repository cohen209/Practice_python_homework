user_string = input("write string: ")

first_char = user_string[0]

last_char = user_string[-1]

middle_index = len(user_string) // 2
middle_char = user_string[middle_index]

print("first_char :", first_char)
print("middle_char :", middle_char)
print("last_char :", last_char)

#  2 משימה 

user_string = input("write string (at least 5 characters): ")

cut_string = user_string[2:]
print("cut string from the 3 letter to the end:", cut_string)

print("string original length:", len(user_string))

modified_string = user_string.replace(" ", "-")
print("string after switching the spaces:", modified_string)