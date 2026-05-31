# שאלה 1 
numbers = []
for i in range(4):
    num = float(input("write a number: ")) 
    numbers.append(num)          

print("the negative numbers are:")
for num in numbers:
    if num < 0:
        print(num)
# שאלה 2
# הגדרת רשימה בסיסית של מילים
words = ["say", "hello", "world", "python"]

print("the list before swapping:", words)

words[0], words[-1] = words[-1], words[0]

print("the list after swapping:", words)


#שאלה 3
grades = [85, 90, 78, 92, 88, 30, 40]

count_passed = 0

for grade in grades:
    if grade >= 70:
        count_passed += 1

print("Number of students who passed:", count_passed)