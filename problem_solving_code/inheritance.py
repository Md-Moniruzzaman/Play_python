import math

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
		
    
    def calculate(self):
        averg = sum(self.scores)/len(self.scores)
	    
        if averg>= 90 and averg<=100:
              return 'O'
        elif averg>= 80 and averg<90:
              return 'E'
        elif averg>= 70 and averg<80:
              return 'A'
        elif averg>= 55 and averg<70:
              return 'P'
        elif averg>=40 and averg<55:
              return 'D'
        elif  averg<40:
              return 'T'
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())