def check_even(x):
    if(x%2==0):
        return 1
list1 =[2,4,5,7,6]
even_list = list(filter(check_even,range(1,21)))
print(even_list)