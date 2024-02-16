# Python Program to Print the Fibonacci sequence

# Fibonacci series
first_term = 0
second_term = 1
terms = int(input("Enter positive terms : "))
print(first_term)
print(second_term)
if(terms>2):
    for i in range(2,terms):
        next_terms = first_term+second_term
        print(next_terms)
        first_term = second_term
        second_term = next_terms