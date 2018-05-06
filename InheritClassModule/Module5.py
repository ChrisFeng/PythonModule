import ClassModule.Module4 as Cm
if __name__ == "__main__":
    print("Module5.py is being run directly")
else:
    print("Module5.py is being imported into another module")

class InheritClass(Cm.classPratice):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id
    def Hello(self):
        return f"InheritClass id is {self.id}, {self.name}"
    