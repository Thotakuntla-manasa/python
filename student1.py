class Student:
    def __init__(self, name, rollno):
        print(self)
        self.name = name
        self.rollno = rollno 
    def hello(self):
        return self.name
s1 = Student(name='Kiran', rollno='342816')
print(s1.rollno)
print(s1.name)
print(s1.hello())