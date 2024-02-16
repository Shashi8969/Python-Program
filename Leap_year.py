y = int(input("Enter year"))
if(y % 400 == 0):
    print("Leap year")
elif(y % 100 != 0):
    if(y % 4 == 0):
        print("Leap year")
    else:
        print("Not leap year")    
else:
    print("Not leap year")