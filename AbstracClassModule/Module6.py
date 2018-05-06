from abc import ABCMeta, abstractmethod

class GuessGame(metaclass=ABCMeta):
    @abstractmethod
    def message(self, msg):
        raise NotImplementedError
    @abstractmethod
    def guess(self):
        raise NotImplementedError

    def go(self):
         self.message(self.welcome)

class ConsoleGame(GuessGame):
    def __init__(self):
        self.welcome = "歡迎"
        self.prompt = "輸入數字"   
    def message(self, meg):
        print(meg)
    def guess(self):
        print("I am guess")