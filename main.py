from abc import ABC, abstractmethod
class Password(ABC):
    def __init__(self, password):
        self.password = str(password)
        self.evaluator = 0
 
    @abstractmethod
    def evaluate(self):
        pass


class PasswordLenght(Password):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        if len(self.password) < 8:
            self.evaluator +=1
        elif 8 <= len(self.password) < 12:
            self.evaluator +=2
        elif 12 < len(self.password):
            self.evaluator +=3

class PasswordUpperCase(Password):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        for i in self.password:
            if i.isupper():
                self.evaluator +=3
                break


            


test = PasswordUpperCase("C1234")

test.evaluate()

print(test.evaluator)