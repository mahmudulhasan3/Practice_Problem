# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(add(20,30,40,50,40,50))


# def introduce(**kwargs):
#     for key,value in kwargs.items():
#         print(f"Key: {key}, Value: {value}")
# introduce(name="Mahmud",ID="CS-2203009",Dept="CSE")


# Challenge 1
# একটা function বানা calculate(operation, *numbers) — operation হবে "add", "multiply", বা "max" — সেই অনুযায়ী কাজ করবে।

# def calculate(operation, *numbers):
#     if operation == "add":
#         total = 0
#         for i in numbers:
#             total += i
#         return total
#     elif operation == "multiply":
#         a = 1
#         for i in numbers:
#             a *= i
#         return a
#     elif operation == "max":
#         return max(numbers)

# print(f"Result = {calculate("max",2,3,4,5,6,6)}")

# Challenge 2
# একটা function বানা build_profile(**info) — যেকোনো key-value নিবে আর একটা সুন্দর formatted string return করবে।

# def build_profile(**info):
#     for key,value in info.items():
#         print(f"{key} - {value}")
# build_profile(name="Mahmud",ID="CS-2203009",dept="CSE",university="NITER")


