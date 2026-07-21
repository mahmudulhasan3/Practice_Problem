# def greet():
#     print("Hello World")
# greet()
# for i in range(1,10):
#     greet()

# def greet(name):
#     print(f"Hello {name}")
# greet("Mahmud")
# greet("Hasan")


# def sum(a,b):
#     print(f"The summation has = {a+b}")
# sum(3,5)
# sum(328,837)

# def add(a,b):
#     return a+b
# result = add(6,8)
# print(result)

# def diff(a,b=20):
#     return a-b
# x = diff(50)
# print(x)

# def sum():
#     x= 10
# sum()
# print(x)

# name = "Hasan"
# def n():
#     print(name)
# n()

# Challenge 1 — Basic function + return
# একটা function বানাও calculate_bmi(weight, height) যেটা BMI return করে।
# BMI = weight / (height * height)
# তারপর result print করো।

# def calculateBMi(weight,height):
#     bmi = weight / height**2
#     return bmi
# print(calculateBMi(60,1.70))

# Challenge 2 — Conditional + return
# একটা function বানাও grade(marks) যেটা marks নিয়ে grade return করে।
# 90+ → "A+", 80+ → "A", 70+ → "B", 60+ → "C", তার নিচে → "F"

# def grade(marks):
#     if marks >= 90 and marks <=100:
#         return "A+"
#     elif marks >= 80:
#         return "A"
#     elif marks >= 70:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     else:
#         return "F"

# print(f"Your grade has: {grade(60)}")

# Challenge 3 — Default parameter
# একটা function বানাও introduce(name, profession="Student") যেটা এভাবে print করে:
# "আমি Rahim, আমি একজন Engineer"
# Default profession হবে "Student".

# def introduce(name,profession="Student"):
#     print(f"I am {name}, I am a {profession}")
# introduce("Mahmud","Engineer")


# Challenge 4 — Scope বোঝো
# নিচের code টা দেখো, বলো output কী হবে এবং কেন:
# pythonx = 5

# def change():
#     x = 10
#     print(x)

# change()
# print(x)
# Output কী? কেন global x বদলায়নি?

# Challenge 5 — Combine করো
# একটা function বানাও shopping_bill(items, discount=0) যেখানে:
# items হবে একটা list যেমন [200, 350, 150]
# সব items এর total বের করবে, তারপর discount বাদ দিয়ে final bill return করবে।
# উদাহরণ: shopping_bill([200, 350, 150], 50) → 650
# এখানে loop use করতে পারবে — sum() নামে Python এর built-in function আছে সেটাও use করতে পারো।

def shopping_bill(items,discount=0):
    sum = 0
    for i in items:
        sum += i
    total_discount = sum * (discount/100)
    total_bill = sum - total_discount
    print(f"Your total bill= {total_bill}")

shopping_bill([200,350,150],50)