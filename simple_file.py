password = input("Enter password")
file = open("Password.txt",'w')
file.write(password)
file.close()
file1 = open("Password.txt",'r')
print(list(file1))
file1.close()



