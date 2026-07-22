# Task: 5 ta variable banao (name, age, height, is_student, price)
# Prottekta variable er type() print koro

# name = "Mahmud"
# age = 23
# height = 23.4
# is_student = True
# # price = 45.9

# print(type(name),type(age),type(height),type(is_student),type(price))

# Task: 5 jon student er marks niye ekta dictionary banao
# student_marks = {"Rafi": 85, ...}
# Highest mark ke pelo ber koro (loop diye, built-in function na use kore)

# student_marks = {
#     "Rafi": 85,
#     "Hasan": 95,
#     "Mahmud": 60,
#     "Karim": 40,
#     "Rahim": 90
# }
# max = 0
# for i in student_marks.values():
#     if i > max:
#         max = i

# print(max)


# Task: grade calculator
# marks >=80 -> A+, >=70 -> A, >=60 -> A-, ... etc
# Input nao, grade print koro

# marks = int(input("Enter your marks: "))
# if marks >= 80:
#     print("A+")


# Task 1: Multiplication table (input number nao, 1-10 porjonto)

# user_input = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{i} x {user_input} = {i*user_input}")
#     i += 1


# Task 2: 1 theke 100 porjonto joog (for loop AND while loop dutai kore dekho)
# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1

# print(sum)

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# Task: Calculator functions banao
# def add(a, b) -> return
# def subtract, multiply, divide (divide by zero handle koro try/except chara-i, just if check)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b == 0:
#         return "Divide by zero"
#     return a/b

# print(add(6,5),sub(6,5),mul(6,5),div(6,5))

# MIXED CHALLENGE
#
# 5 jon student er info niye ekta list of dictionaries banao:
# students = [
#     {"name": "Rafi", "marks": 85},
#     {"name": "Hasan", "marks": 45},
#     ... (5 jon)
# ]
#
# Task 1: ekta function likho "get_grade(marks)"
#         ja marks er upor base kore grade return korবে (A+, A, A-, Fail etc.)
#
# Task 2: for loop diye protita student er upor loop koro,
#         get_grade() function call koro,
#         output print koro এইভাবে: "Rafi - 85 - A+"
#
# Task 3: ekta function likho "class_average(students)"
#         ja shob student er marks er average ber kore return korবে
#
# Task 4: jei student er marks sobcheye kom (fail er kachakachi),
#         tar naam print koro (loop diye ber koro, built-in min() use na kore)


student = [
    {"name": "Rafi", "marks": 85},
    {"name": "Hasan", "marks": 80},
    {"name": "Mahmud", "marks": 60},
    {"name": "Rahim", "marks": 50},
    {"name": "Karim", "marks": 90},
]

def get_marks(mark):
    if mark >= 80:
        return "A+"

print(get_marks(student["name":"Rahim"]))

