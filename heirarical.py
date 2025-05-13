class Parent:
    def func1(self):
        print("This is the Parent class.")
class Child1(Parent):
    def func2(self):
        print("This is the Child1 class.")
class Child2(Parent):
    def func3(self):
        print("This is the Child2 class.")
parent = Parent()
child1 = Child1()
child2 = Child2()
parent.func1()
child1.func1()
child1.func2()
child2.func1()
child2.func3()