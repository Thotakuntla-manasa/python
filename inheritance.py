class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name
    def show_grandfather(self):
        print(f"Grandfather's Name: {self.grandfather_name}")
class Father(Grandfather):
    def __init__(self, grandfather_name, father_name):
        super().__init__(grandfather_name)
        self.father_name = father_name
    def show_father(self):
        print(f"Father's Name: {self.father_name}")
class Daughter(Father):
    def __init__(self, grandfather_name, father_name, daughter_name):
        super().__init__(grandfather_name, father_name)
        self.daughter_name = daughter_name

    def show_daughter(self):
        print(f"Daughter's Name: {self.daughter_name}")
s = Daughter("Krishna", "Manjunath", "Manasa")
s.show_grandfather()
s.show_father()
s.show_daughter()