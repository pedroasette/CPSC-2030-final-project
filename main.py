from abc import ABC, abstractmethod
class Password(ABC):
    def __init__(self, password):
        self.password = password
        self.evaluator = 0
 
    @abstractmethod
    def evaluate(self):
        pass


class PasswordLenght(Password):
    def __init__(self, password):
        super().__init__(password)
    def evaluate(self):
        if len(str(self.password)) < 8:
            self.evaluator +=1
        elif 8 <= len(str(self.password)) < 12:
            self.evaluator +=2
        elif 12 < len(str(self.password)):
            self.evaluator +=3
            


test = PasswordLenght(12345678912345)

test.evaluate()

print(test.evaluator)