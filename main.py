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
    @abstractmethod
    def report(self):
        pass

#base class
class PasswordPatterns(ABC):
    def __init__(self, password, score):
        self.password = str(password)
        self.final_score = score
        self.decrease = 0
        
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def report(self):
        pass
    
class Evaluator(ABC):
    @abstractmethod
    def finalEvaluate():
        pass

#check the password lenght
class PasswordLenght(PasswordRequisites):
    def __init__(self, password):
        super().__init__(password)
    def evaluate(self):
        if 4 <= len(self.password) < 8:
            self.evaluator +=15
        elif 8 <= len(self.password) < 12:
            self.evaluator +=30
        elif 12 <= len(self.password):
            self.evaluator +=40
    
    def report(self):
        if  len(self.password) < 8:
            return "Your password is short"
        else: 
            pass


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

    def report(self):
        if self.evaluator != 15:
            return "Your password has no Upper Case character"
        else: 
            pass

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

    def report(self):
        if self.evaluator != 15:
            return "Your password has no lower case character"
        else: 
            pass


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

    def report(self):
        if self.evaluator != 15:
            return "Your password has no numbers"
        else: 
            pass

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

    def report(self):
        if self.evaluator != 15:
            return "Your password has no special character"
        else: 
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

    def report(self):
        if self.decrease != 0:
            return "Your password is a common password"
        else: 
            pass


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

    def report(self):
        if self.decrease != 0:
            return "Your password has a repetition pattern"
        else: 
            pass

        
#Check if the password is a date, IT NEEDS TO BE FIXED
class PasswordDate(PasswordPatterns):
    def __init__(self, password, score):
        super().__init__(password, score)

    def evaluate(self):
        with open("dates.txt", "r") as date:
            dates = date.read().splitlines()  # lines like "0101", "2506", etc.
            years = [str(y) for y in range(1920, 2026)]  # proper list of strings

        for x in dates:
            for y in years:
                if x + y in self.password:
                    if self.final_score == 45:
                       self.decrease +=15
                    else: 
                        self.decrease +=10

                  
                    
            
    
    def report(self):
        if self.decrease != 0:
            return "Your password is or contain a date"
        else: 
            pass


                        

#combine all the evaluators
class PasswordEvaluator(Evaluator):
    def __init__(self, password):
        self.password = password
        self.score = 0
        self.criterias = [PasswordLenght(password), PasswordUpperCase(password), PasswordLowerCase(password), PasswordNumber(password), PasswordSpecialCharacter(password)]
        self.report=[]

    def finalEvaluate(self):
        for i in self.criterias:
            i.evaluate()
            if i.report() != None:
                self.report.append(i.report())

            self.score += i.evaluator

        return self.score


#combine all the evaluators
class FinalPasswordEvaluator(Evaluator):
    def __init__(self, password, score):
        self.password = password
        self.score = score
        self.criterias = [CommonPasswords(password, score), PasswordRepetition(password, score), PasswordDate(password, score)]
        self.report = []

    def finalEvaluate(self):
        for i in self.criterias:
            i.evaluate()
            if i.report() != None:
                self.report.append(i.report())

            self.score -= i.decrease
            if 1 <= len(self.password) <= 3:
                self.score = 8
            if self.score < 0:  
                self.score = 0
            

        return self.score


def run_program():
    #PUT YOUR PASSWORD HERE
    password = input("Enter your password here: ")
    psswrd = PasswordEvaluator(password)
    score = psswrd.finalEvaluate()
    report1 = psswrd.report

    evaluator = FinalPasswordEvaluator(password, score)
    finalscore = evaluator.finalEvaluate()
    report2 = evaluator.report
    report = report1 + report2
    print(f"Your final score is {finalscore}!")
    if len(report) > 0:
        print("The weaknesses of your passwords are:")
        for i in report:
            print(i)
    else:
        print("Your password has no weaknesses!")


run_program()