class Parent1:
    def func1(self):
        print("This is from Parent1")
class Parent2:
    def func2(self):
        print("This is from Parent2")
class Child(Parent1, Parent2):
    def func3(self):
        print("This is from Child")
child = Child()
child.func1()  
child.func2()  
child.func3()  