class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def calculate_avg(self):
        return (self.marks1 + self.marks2 + self.marks3) / 3
student1 = Student(name="John", m1=85, m2=90, m3=88)
print(f"Student Name: {student1.name}")
print(f"Avg Marks: {student1.calculate_avg()}")
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)

    def calculate_avg(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

student = Student("John Doe")
student.add_marks(85)
student.add_marks(90)
student.add_marks(78)

avg = student.calculate_avg()
print(f"Student Name: {student.name}")
print(f"Avg Marks: {avg}")