if __name__ == "__main__":
    print("Module4.py is being run directly")
else:
    print("Module4.py is being imported into another module")

class classPratice():
    def __init__(self, name = 'I am father'):
        self.name = name
    def Hello(self):
        return self.name
    def __privatefunction(self):
        return f"I am private function and name is {self.name}"
    def getprivate(self):
        return self.__privatefunction()
    def __str__(self):
        return f'classPratice name is {self.name}'