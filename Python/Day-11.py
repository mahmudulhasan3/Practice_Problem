# with open("marks.txt","w") as file:
#     file.write("Mahmudul Hasan")

# with open("marks.txt", "r") as file:
#     print(file.read())
# with open("marks.txt", "a") as file:
#     file.write("\nDepartment of CSE")

# student = {
#     "Mahmud": 90,
#     "Hasan": 80
# }

# import json
# # with open("data.json", "w") as file:
# #     json.dump(student,file)

# # with open("data.json", "r") as file:
# #     print(json.load(file))

# data = json.dumps(student)
# print(type(data))
# new = json.loads(data)
# print(new)

import json

student = {"name": "Mahmud", "marks": 85, "grade": "A"}

with open("student.json", "w") as file:
    json.dump(student,file)

with open("student.json", "r") as file:
    print(json.load(file))

data = json.dumps(student)
print(data)
text = json.loads(data)
print(text)
