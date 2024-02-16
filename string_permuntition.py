from itertools import permutations

words = input("Enter words - ")
 
# Finding all permutation
permutation = [''.join(i) for i in permutations(words)]
# Printing result
print("Resultant List", str(permutation))