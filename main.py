from abc import ABC, abstractmethod
#Base class
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
            self.evaluator +=1 #value will change in the future
        elif 8 <= len(self.password) < 12:
            self.evaluator +=2 #value will change in the future
        elif 12 < len(self.password):
            self.evaluator +=3 #value will change in the future


class PasswordUpperCase(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i.isupper():
                count +=1

        if count == len(self.password) or count == 0:
            self.evaluator +=1 #value will change in the future
        else:
            self.evaluator +=3 #value will change in the future


class PasswordLowerCase(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i.islower():
                count +=1

        if count == len(self.password) or count == 0:
            self.evaluator +=1 #value will change in the future
        else:
            self.evaluator +=3 #value will change in the future


#Class that will combine all the properties in actual evaluation
class PasswordEvaluator:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.criterias = [PasswordLenght(password), PasswordUpperCase(password), PasswordLowerCase(password)]

    def finalEvaluate(self):
        for i in self.criterias:
            i.evaluate()
            self.score += i.evaluator

        return self.score
            
test = PasswordEvaluator("Pa197370")
test.finalEvaluate()
print(test.score)