def is_palindrome(s): 
 s = s.lower() 
 reversed_s = s[::-1] 
 return s == reversed_s 
def main(): 
 string = input("Enter a string: ") 
 if is_palindrome(string): 
    print(f"{string} is a palindrome.") 
 else: 
    print(f"{string} is not a palindrome.") 
main() 