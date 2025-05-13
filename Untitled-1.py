class NAG:
    def __init__(self):
        self.name = "Nagarjuna"
    def show(self):
        print(f"I am {self.name}")
class Naga_chaitanya(NAG):
    def __init__(self):
        super().__init__()  
        self.son_name = "NagaChaitanya"
    def show(self):
        super().show()
        print(f"I am the son: {self.son_name}")
class Akhil(NAG):
    def __init__(self):
        super().__init__()
        self.son_name = "Akhil"
    def show(self):
        super().show()
        print(f"I am the son: {self.son_name}")
naga_chaitanya = Naga_chaitanya()
Akhil = Akhil()
naga_chaitanya.show()
print()
Akhil.show()