#Find the distance of two point(x1,y1) and (x2,y2)
#Distance = ((x2-x1)**2 + (y2-y1)**2)*0.5)

def dist(x1,x2,y1,y2):
    d = (((x2-x1)**2 + (y2-y1)**2)**0.5)
    return d
x1 = float(input("x1 : "))
x2 = float(input("x2 : "))
y1 = float(input("y1 : "))
y2 = float(input("y2 : "))
#Calling function
distance = dist(x1,x2,y1,y2)
print(distance)