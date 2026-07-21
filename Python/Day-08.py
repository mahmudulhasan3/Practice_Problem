# even = []
# for i in range(1,100):
#     if i % 2 == 0:
#         even.append(i)
# print(f"The even numbers are: {even}")

# square = []
# for i in range(1,10):
#     square.append(i**2)
# print(square)

# # Example 1 — সংখ্যার square:
# square = [x**2 for x in range(1,10)]
# print(square)

# Example 2 — সবকিছু double করো:

# double = [x*2 for x in range(1,11)]
# print(double)

# number = [1,2,3,4,5]
# square_dict = []
# result = {x: x**2 for x in number}
# print(result)

# student_info = {
#     "name": "Mahmud",
#     "id": 22,
#     "dept": "CSE"
# }

# result = {k:v for k,v in student_info.items()}
# print(result)


# Problem 1 — Easy
# pythonnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# এই list থেকে শুধু বিজোড় সংখ্যাগুলো বের করো। ➡️ List Comprehension দিয়ে।

# python_numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_numbers = [x for x in python_numbers if x%2 != 0]
# print(odd_numbers)

# Problem 2 — Easy
# pythonnames = ["mahmud", "alice", "bob", "charlie"]
# সব নাম uppercase করো। ➡️ List Comprehension দিয়ে।

# names = ["mahmud","alice","bob","charlie"]
# names_uppercase = [x.upper() for x in names]
# print(names_uppercase)

# Problem 3 — Medium
# pythonnumbers = [1, 2, 3, 4, 5]
# প্রতিটা number → তার square এর dict বানাও।
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# numbers = [1,2,3,4,5]
# output = {k:k**2 for k in numbers}
# print(output)

# Problem 4 — Medium
# pythonscores = {"Mahmud": 85, "Alice": 40, "Bob": 72, "Charlie": 30}
# শুধু pass করা students রাখো (50 এর উপরে)। ➡️ Dict Comprehension দিয়ে।

# scores = {
#     "Mahmud": 85,
#     "Alice": 40,
#     "Bob": 72,
#     "Carlie": 30
# }
# output = {k:v for k,v in scores.items() if v > 50}
# print(output)

# Problem 5 — Hard
# pythonscores = {"Mahmud": 92, "Alice": 74, "Bob": 55, "Charlie": 38}
# প্রতিটা student কে grade দাও:

# 80+ → "A"
# 60+ → "B"
# 40+ → "C"
# বাকি → "F"

# ➡️ Dict Comprehension দিয়ে।

marks = {
    "Mahmud": 92,
    "ALice": 74,
    "Bob": 55,
    "Charlie": 38
}
output = {
    k: "A" if v >= 80 else "B" if v >= 60 else "C" if v >= 50 else "F"
    for k, v in marks.items()
}
print(output)