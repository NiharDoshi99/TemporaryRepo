class Person:
    name = "Nihar"
    def __init__(self) -> None:
        print("invoked")

    def getName(self):
        return self.name

    def changeName(self, newName):
        self.name = newName


p1 = Person()
p1.changeName("SAM")
print(p1.getName())

