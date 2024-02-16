# Write a program to find the median of the tuples.

def get_median(t):
    # sort the tuple and store the resulting list
    asc_t = sorted(t)
    # find the median
    if len(asc_t) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(asc_t)+1)/2 - 1)
        print(m)
        return asc_t[m]
    else:
        m1 = len(asc_t)//2 - 1
        m2 = len(asc_t)//2
        print(m2)
        return (asc_t[m1]+asc_t[m2])/2
# create a tuple
t = (5, 2, 1, 4,6,9)
# get the median
print(get_median(t))