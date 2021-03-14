"""
THEORITCALLY correct, so inefficient laptop crashes for n>11
"""
#Permutations
import itertools
def MaxSteps(n):
    tmp=0
    for i in range(2,n+1):
        if tri(i)<=n:
            tmp=i
    return tmp
def tri(x):
    sum=0
    for i in range(1,x+1):
        sum += i
    return sum
    #return x + tri(x-1)

def solution(n):
    Max=MaxSteps(n)
    lst=[]
    m=n
    if n>15:
        m=n//2+1
    elif n>60:
        m=n//6+1
    elif n>70:
        m=n//7+1
    elif n>80:
        m=n//8+1
    elif n>90:
        m=n//9+1
    elif n>100:
        m=n//10+3
    for i in range (1,m):
        lst.append(i)
    permutations=[]
    for i in range(2,n):
        permutations += itertools.permutations(lst,i)
    okLength=[]
    for tation in permutations:
        if len(tation)<=Max:
            okLength.append(tation)
    # print(okLength)
    okSum=[]
    for lengtup in okLength:
        if sum(lengtup)==n:
            okSum.append(lengtup)
    # print(okSum)
    okOrder=[]
    for sumtup in okSum:
        lessThan=False
        for i in range(0,len(sumtup)-1):
            if sumtup[i]>sumtup[i+1]:
                lessThan=True
        if lessThan==False:
            okOrder.append(sumtup)
    # print(okOrder)
    return len(okOrder)
for i in range(3,11):
    print(i,solution(i),MaxSteps(i))