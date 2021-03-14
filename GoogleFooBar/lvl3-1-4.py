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
#Iteration!!!!!!!!

def solution1(n):
    lst=[]
    counter=0
    for i in range (1,n+1):
        if i<n-i:
            lst.append((i,n-i))
            counter+=1
        else:
            break
    for j in range(1,n):
        m=n-j
        if j<m:
            for i in range(j+1,m+1):
                if i<m-i:
                    lst.append((j,i,m-i))
                    counter+=1
                else:
                    break
        else:
            break
    for i in range(1,n):
        m=n-i
        if i<m:
            for j in range(i+1,m):
                l=m-j
                if j<l-j:
                    for k in range(j+1,l):
                        o=l-k
                        if k<o:
                            lst.append((i,j,k,l-k))
                            counter+=1
                        else:
                            break
                else:
                    break
        else:
            break
    return((lst,counter))
print(solution1(17))
print("")

#recursion

def solution(n):
    M=MaxSteps(n)
    count=[]
    for i in range(2, M+1):
        sol=recursolution(n,i,0)
        for each in sol:
            count.append(each)
    return (count, len(count))

def recursolution(size,Max,step):
    step+=1
    if Max==2:
        lst=[]
        for i in range (step,size+1):
            if i<size-i:
                lst.append((i,size-i))
            else:
                break
        return lst
    else:
        out=[]
        for i in range(step,Max+1):
            tmp=recursolution(size-i,Max-i+1,i)
            for each in tmp:
                out.append((i,each))
        return out

print(solution(17))


# else:
#         out=[]
#         for i in range(step,Max+1):
#             tmp=recursolution(size-i,Max-1,i)
#             for each in tmp:
#                 out.append((i,each))
#         return out

# else:
#         out=[]
#         tmp=recursolution(size-step,Max-1,step)
#         for each in tmp:
#             out.append((step,each))
#         return out