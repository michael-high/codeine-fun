# You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

# You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] > right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def swap(lst,i,j):
    tmp=lst[i]
    lst[i]=lst[j]
    lst[j]=tmp
lst=[3,1,4,1,5,9]

def solution(L):
    if len(L)==1:
        if L[0]%3==0:
            return L[0]
        return 0
    FirstSort=merge_sort(L)#Largest to smallest
    print(FirstSort)
    if sum(FirstSort)%3==0:
        return int("".join(map(str, FirstSort)))
    else:
        for i in range(1,len(FirstSort)-1):
            if sum(FirstSort[0:-1])%3==0:
                return int("".join(map(str, FirstSort[0:-1])))
            else:
                swap(FirstSort,-1,-1-i)
            print(FirstSort)
    SecondSort=merge_sort(FirstSort)
    return solution(SecondSort[0:-1])

print(solution(lst))