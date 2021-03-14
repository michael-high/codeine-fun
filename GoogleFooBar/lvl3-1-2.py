def two(n):
    offset=1
    rest=n-1
    counter=0
    while offset<rest:
        counter+=1
        offset+=1
        rest-=1
    return counter
def three(n,M):
    counter=0
    if n//3 >1.0:
        for i in range(0, n//3 +1):
            counter+=two(n-i)-i
        counter+=two(n-2)-2
    else:
        return two(n)
    return counter

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
    print(Max, n)
    return three(n,Max)
    
print(solution(3))

for i in range(3,201):
    print(i,MaxSteps(i))
