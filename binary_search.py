import random
import time

# implementation of binary search algorithm
# we will prove the binary search is faster than the naive search

# Naive search: scan entire list and ask if it is equal to the target
def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary Search uses divide and conquer
# we leverage the fact that our list is SORTED
def binary_search(l,target,low=None,high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l)
    if high < low:
        return -1
    midpoint = (low+high)//2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:
        return binary_search(l,target,midpoint+1,high)
    else:
        return binary_search(l,target,low,midpoint-1)


def main():
    
    length = 10000
    # build a sorted list of length 10000
    sorted_list =  set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()
    print("Naive search time: ",(end - start)/length," seconds.")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()
    print("Binary search time: ",(end - start)/length," seconds.")

if __name__ == "__main__":
    main()