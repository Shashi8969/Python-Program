# File handling operations in python.
class student:
    def __init__(self):
        self.name = input("Enter name - ")
        self.roll = input("Enter roll no. -")
    
    def store(self):
        file = open("Student.txt",'a')
        file.write(self.name)
        file.write(self.roll)
        file.close()
        print("Data store successfully")
    def over_ride(self):
        file = open("Student.txt",'w')
        file.write(self.name)
        file.write(self.roll)
        file.close()
        print("Data override successfully")
    def print_file(self):
        try:
            file1 = open("Student.txt","r")
            print(list(file1))
            file1.close()
        except:
            print("File does not exist.")

b1 = student()

# b1.store()
b1.print_file()
# b1.over_ride()