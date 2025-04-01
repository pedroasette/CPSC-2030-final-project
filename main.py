from abc import ABC, abstractmethod
from datetime import datetime

#base class
class PasswordRequisites(ABC):
    def __init__(self, password):
        self.password = str(password)
        self.evaluator = 0
 
    @abstractmethod
    def evaluate(self):
        pass

#check the password lenght
class PasswordLenght(PasswordRequisites):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        if 0 < len(self.password) < 4:
            self.evaluator +=5
        elif 4 <= len(self.password) < 8:
            self.evaluator +=15
        elif 8 <= len(self.password) < 12:
            self.evaluator +=25
        elif 12 <= len(self.password):
            self.evaluator +=40

#check if it has at least 1 upper case
class PasswordUpperCase(PasswordRequisites):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i.isupper():
                count +=1

        if count > 0:
            self.evaluator +=15

#check if it has at least 1 lower case
class PasswordLowerCase(PasswordRequisites):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i.islower():
                count +=1

        if count > 0:
            self.evaluator +=15

#check if it has at least 1 number
class PasswordNumber(PasswordRequisites):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i in "0123456789":
                count +=1

        if count > 0:
            self.evaluator +=15

 #check if it has at least 1 special character       
class PasswordSpecialCharacter(PasswordRequisites):
    def __init__(self, password):
        super().__init__(password)

    def evaluate(self):
        count = 0
        for i in self.password:
            if i in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":

                count +=1
        
        if count > 0:
            self.evaluator +=15

#combine all the evaluators
class PasswordEvaluator:
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.criterias = [PasswordLenght(password), PasswordUpperCase(password), PasswordLowerCase(password), PasswordNumber(password), PasswordSpecialCharacter(password)]

    def finalEvaluate(self):
        for i in self.criterias:
            i.evaluate()
            self.score += i.evaluator

        return self.score


#base class
class PasswordPatterns(ABC):
    def __init__(self, password, score):
        self.password = str(password)
        self.final_score = score
        self.decrease = 0
        
 
    @abstractmethod
    def evaluate(self):
        pass


#check if it is a common used password
class CommonPasswords(PasswordPatterns):
    def __init__(self, password, score):
        super().__init__(password, score)
    
    def evaluate(self):
        with open("commonPasswordList.txt", "r") as plist:                 
            p = plist.read().splitlines()

            count = 0
            for i in p:
                if i.strip() == self.password.strip():
                    count +=1
                    break
            
            if count != 0:
                if self.final_score >= 50:
                    self.decrease += 25
                elif self.final_score < 50:
                    self.decrease += 15

          

#check if the password repeat the same character multiple times
class PasswordRepetition(PasswordPatterns):
    def __init__(self, password, score):
        super().__init__(password, score)

    def evaluate(self):
        count = 0
        for i in range(len(self.password) - 2):
            if self.password[i] == self.password[i + 1] == self.password[i + 2]:
                count +=1
                break
        if count != 0:
            if self.final_score >= 50:
                    self.decrease += 25
            elif self.final_score < 50:
                    self.decrease +=10

            
""""
#Check if the password is a date, IT NEEDS TO BE FIXED
class PasswordDate(PasswordPatterns):
    def __init__(self, password, score):
        super().__init__(password, score)
    

""" 


#combine all the evaluators
class FinalPasswordEvaluator:
    def __init__(self, password, score):
        self.password = password
        self.score = score
        self.criterias = [CommonPasswords(password, score), PasswordRepetition(password, score)]

    def finalEvaluate(self):
        for i in self.criterias:
            i.evaluate()
            self.score -= i.decrease
            if self.score < 0:  
                self.score = 0
        return self.score

password = "123467890bvC@"
            
psswrd = PasswordEvaluator(password)
score = psswrd.finalEvaluate()
print(score)


test = FinalPasswordEvaluator(password, score)
print(test.finalEvaluate())