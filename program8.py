# Write a program for finding whether the string is palindrome or not.

def check_palin (str):
    for i in range (0, int (len (str)/2)):
        if str [i] != str [len (str) -i-1]:
            return 0
        return 1
    
str_1 = input("Enter a string -")
ans = check_palin (str_1)
if (ans):
        print ("Yes, it is a palindrome.")
else:
        print ("No, it is not a palindrome.")
