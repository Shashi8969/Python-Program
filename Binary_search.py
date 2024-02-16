list_1 = [1,2,3,4,5,6,7,2,5]   #defined a list 
list1 = sorted(list_1)      #Sorted the list in ascending order.
print("Sorted list is ",list1)      
start = 0  #starting index of list
end = len(list1)-1  #ending index in list
found = 0  #It works when value is find in list.
value = int(input("enter number to find place -"))
# Use while loop and write a condition.
while(start<=end): #loop is running when start is less then end index.
    mid =(start+end)//2    #find middle index in list.
    if(list1[mid]==value):      #Check condition when list of middle item is equal to value
        print("{} is {}th place in list ".format(value,mid+1))  # Print the position and break the loop.
        found =1  #Here found is assign 1.
        break   
    elif(value >list1[mid]):  #when value is less and list of middle index value is bigger.
        start = mid+1   #Assign middle index + 1 to start index.
    else:   #When value is greater the middle index value
        end = mid-1  #Assign end index to middle index -1.
    if(start > end and found ==0):  #when start index is greater and found is equal to 0
        print("{} does not exist in the list.".format(value))  #value is not exist.
       
        
        
