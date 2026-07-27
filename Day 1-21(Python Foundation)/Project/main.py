class Student:
    def __init__(self, name: str, roll: str, marks: dict):
        self.name = name
        self.roll = roll
        self.marks = marks

    def add_marks(self):
        while True:
            self.subject = input("Enter subject name: ")
            if self.subject == "quit":
                break
            try:
                self.mark = int(input("Enter mark: "))
            except ValueError as e:
                print(e)
            self.marks[self.subject] = self.mark
        return self.marks

    def average(self):
        sum = 0
        for i in self.marks.values():
            sum += i
        avg = sum / len(self.marks)
        return avg


class GraduateStudent(Student):
    def __init__(self, name: str, roll: str, marks: dict, thesis_title):
        super().__init__(name, roll, marks)
        self.thesis_title = thesis_title

    def save(self):
        import json

        with open("student_all.json", "w") as file:
            return json.dump(self.marks, file)


