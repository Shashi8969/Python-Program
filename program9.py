# Write a function for breaking the set into the list of the sets.
set1 = {1,2,3,4,5}
list1 =[]
set2 =list(set1)

for i in range(0,len(set2)):
    list1.append(set(str(set2[i])))
    
# print(set1[1])    
print(list1)

def set_of_list(set1):
    list1 = [{i} for i in set1]
    print("List of sets -",list1)
#Create a set of element.
set1 = {"Amit","Rishi","Rakesh"}
set_of_list(set1)