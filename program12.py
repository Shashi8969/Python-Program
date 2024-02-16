# Write a program in Python that takes the name, roll number, and marks of a student and calculates their percentage, and prints the grade to demonstrate class, object and methods in python.

class student:
    total = 0
    def __init__(self):
        self.name = input("Enter name - ")
        self.roll = input("Enter roll no -")
    def user_marks(self):
        self.math = int(input("Enter mathematics subject marks -"))
        self.eng = int(input("Enter english subject marks -"))
        self.science = int(input("Enter science sub -"))
        self.total = self.math+self.eng+self.science
    def calculate(self):
        self.per = self.total/400*100
        print("Total marks -",self.total,"and percentage ",self.per)
st1 = student()
st1.user_marks()
st1.calculate()
st2 = student()
st2.user_marks()
st2.calculate()
