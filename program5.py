# Write a program to verify the number is odd, even or prime.
def check_prime(num):
    if(num==1):
        print(num,"is not a prime number")
    elif(num>1):
        for i in range(2,num):
            if(num%i)==0:
                print(num,"is not a prime number")
                break
            else:
                print(num,"is prime number")
                break
    else:
        print("Number is not a prime")

def check_odd(num):
    if(num%2==0):
        print(num,"is even number")
    else:
        print(num,"is odd number")

num1 = int(input("Enter number -"))
check_prime(num1)
check_odd(num1)