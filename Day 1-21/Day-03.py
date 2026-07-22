# list = [1,2,3,4,5,6]
# print(list)
# print(list[2])

# tuple = (1,2,3,4,5)
# print(tuple)
# print(type(tuple))

# set = {10,1,2,3,4,5,5,6}
# print(set)
# print(type(set))

# dict = {"Mahmud": 23}
# print(dict)
# print(type(dict))

# marks = [80,60,70,85,90,97,85]
# print(marks[2])
# print(marks[1:4])
# print(marks[:5])
# print(marks[1:6:2])
# print(marks[-1])

# marks.append(96)
# print(marks)
# marks.insert(1,40)
# print(marks)
# marks.remove(96)
# print(marks)
# marks.sort()
# print(marks)
# print(len(marks))


# studentInfo = ("Mahmud",9,"CSE")
# print(studentInfo[0])
# studentInfo[0]="Hasan"
# print(studentInfo)


# marks = [80,60,70,85,90,97,80,70,85]
# newMarks = set(marks)
# print(type(newMarks))
# print(newMarks)

# section_a_pass = {"Rahim", "Karim", "Jamal"}
# section_b_pass = {"Karim", "Nabil", "Rahim"}

# common = section_a_pass & section_b_pass
# print(common)
# difference = section_a_pass - section_b_pass
# print(difference)

# studentMarks = {
#     "Mahmud": 90,
#     "Hasan": 85,
#     "Jubair": 80,
#     "Jamal": 86,
#     "Rahim": 70
# }
# print(studentMarks["Mahmud"])
# print(studentMarks.get("Karim"))
# studentMarks["Mahmud"]=60
# print(studentMarks)
# studentMarks["Karim"]=87
# print(studentMarks)
# del studentMarks["Jamal"]
# print(studentMarks)
# print(studentMarks.keys())
# print(studentMarks.values())

# একটা dict বানাও 5 জন student এর নাম আর marks দিয়ে। তারপর একজনের marks update করো, একজনকে বাদ দাও, একজন নতুন যোগ করো।

# student = {
#     "Mahmud": 90,
#     "Hasan": 86,
#     "Jubair": 80,
#     "Rahim": 96,
#     "Karim": 85
# }
# print(f"The dictionary has: {student}")
# student["Hasan"]=94
# print(f"Updated dictionary: {student}")
# del student["Jubair"]
# print(f"After Deleting: {student}")
# student["Alif"] = 84
# print(f"After adding new student: {student}")

# একটা list নাও যেখানে কিছু duplicate marks আছে। সেটাকে set এ convert করো আর print করো।
# marks = [90,70,80,84,80,70,65,90,95]
# newMarks = set(marks)
# print(newMarks)


# Practice 1
student_marks = {
    "Rahim": 85,
    "Karim": 90,
    "Jamal": 72,
    "Nabil": 65,
    "Suman": 88,
}
# student_marks theke shudhu marks gulo ber koro
# student_marks theke shudhu name gulo ber koro
# "Raju" dict e ache kina check koro — get() use kore

# print(student_marks.values())
# print(student_marks.keys())
print(student_marks.get("Raju","Not Found"))


# Practice 2
fruits = ["apple", "banana", "mango", "apple", "banana", "orange"]
# duplicate bad diye unique fruits ber koro
# set theke list e convert koro

# newFruits = set(fruits)
# print(newFruits)
# againConvert = list(newFruits)
# print(againConvert)


# Practice 3
student1 = ("Rahim", 101, 85)
student2 = ("Karim", 102, 90)
# duijoner name print koro
# duijoner marks print koro
# duita marks ekta list e rakho

print(student1[0],student2[0])
print(student1[2],student2[2])
newList = [student1[2],student2[2]]
print(newList)