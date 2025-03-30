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
        if 4 <len(self.password) < 8:
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

        if count > 0:
            self.evaluator +=1 #value will change in the future


class PasswordLowerCase(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i.islower():
                count +=1

        if count > 0:
            self.evaluator +=1 #value will change in the future


class PasswordNumber(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i in "0123456789":
                count +=1

        if count > 0:
            self.evaluator +=1 #value will change in the future
        
class PasswordSpecialCharacter(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":

                count +=1
        
        if count > 0:
            self.evaluator +=1 #value will change in the future

class CommonPasswords(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)
    
    def evaluate(self):
        with open("commonPasswordList.txt", "r") as plist:                 
            p = plist.read().split()

            count = 0
            for i in p:
                if i == self.password:
                    count +=1
            
            if count == 0:
                self.evaluator +=1 #value will change in the future

class PasswordRepetition(PasswordProperty):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in range(len(self.password) - 2):
            if self.password[i] == self.password[i + 1] == self.password[i + 2]:
                count +=1
        if count == 0:
            self.evaluator +=1 #value will change in the future


class PasswordEvaluator:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.criterias = [PasswordLenght(password), PasswordUpperCase(password), PasswordLowerCase(password), PasswordNumber(password), PasswordSpecialCharacter(password), CommonPasswords(password), PasswordRepetition(password)]

    def finalEvaluate(self):
        if len(self.password) < 4:
            pass
        else:
            for i in self.criterias:
                i.evaluate()
                self.score += i.evaluator

        return self.score
            
test = PasswordEvaluator("")
print(test.finalEvaluate())

