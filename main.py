from abc import ABC, abstractmethod
class PasswordProperty(ABC):
    def __init__(self, password):
        self.password = str(password)
        self.evaluator = 0
 
    @abstractmethod
    def evaluate(self):
        pass

class PasswordLenght(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        if len(self.password) < 8:
            self.evaluator +=1
        elif 8 <= len(self.password) < 12:
            self.evaluator +=2
        elif 12 < len(self.password):
            self.evaluator +=3

class PasswordUpperCase(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i.isupper():
                count +=1

        if count == len(self.password) or count == 0:
            self.evaluator +=1
        else:
            self.evaluator +=3

class PasswordEvaluator:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.criterias = [PasswordLenght(password), PasswordUpperCase(password)]

    def finalEvaluate(self):
        for i in self.criterias:
            i.evaluate()
            self.score += i.evaluator


        return self.score
            



            


test = PasswordEvaluator("1234")

test.finalEvaluate()

print(test.score)