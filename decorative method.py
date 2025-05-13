class Student:
    college_name = "SVCET"  
    def __init__(self, name, rollno):  
        print(Student)
        self.name = name
        self.rollno = rollno 

    @staticmethod
    def hello():
        print("Good afternoon")
s1 = Student(name='virat', rollno='18')
s1.hello() 