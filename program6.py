# Write a program to find out the positive and negative number in list.

list1 = [1,2,-3,4,-5]
pos=[]
neg=[]

for i in list1:
    if(i>0):
        pos.append(i)
    elif(i<0):
        neg.append(i)
    else:
        print(i,"Number is nor positive neither negative")
print("Positive list - ",pos)
print("Negative list - ",neg)