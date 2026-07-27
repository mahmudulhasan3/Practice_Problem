import main

student = main.GraduateStudent("Mahmud", "CS-2203009", {"Hasna": 23, "Mahmud": 45}, "No")
student.save()
print(student.add_marks())

print(student.average())
def get_grade():
    if student.average() >= 80:
        print("A+")
    elif student.average() >=70 and student.average() < 80:
        print("A")
    elif student.average() >=60 and student.average() < 70:
            print("B")
    elif student.average() >=50 and student.average() < 60:
            print("C")
    elif student.average() >=40 and student.average() < 50:
            print("D")
    elif student.average() < 40 and student.average() <= 0:
            print("F")
    else:
          print("Invalid")

get_grade()
    