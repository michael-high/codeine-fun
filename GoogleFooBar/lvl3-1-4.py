def MaxSteps(n):
    tmp=0
    for i in range(2,n+1):
        if tri(i)<=n:
            tmp=i
    return tmp
def tri(x):
    suM=0
    for i in range(1,x+1):
        suM += i
    return suM
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
    for i in range(1,n):
        m=n-i
        if i<m:
            for j in range(i+1,m):
                l=m-j
                if j<l-j:
                    for k in range(j+1,l):
                        o=l-k
                        if k<o-k:
                            for h in range(k+1,o):
                                p=o-h
                                if h<p-h:
                                    lst.append((i,j,k,h,p-h))
                                    counter+=1
                                else:
                                    break
                        else:
                            break
                else:
                    break
        else:
            break
    return((lst,counter))
print(solution1(15))
print("")

#recursion

def solution(n):
    M=MaxSteps(n)
    count=[]
    # total=0
    for i in range(2, M+1):
        # total+=recursolution(n,i,0)
        sol=recursolution(n,i,0)
        for each in sol:
            count.append(each)
    return (count, len(count)) #total

def recursolution(size,Max,step):
    # count=0
    step+=1
    if Max==2:
        lst=[]
        for i in range (step,size+1):
            if i<size-i:
                lst.append((i,size-i))
                # count+=1
            else:
                break
        return lst  #count
    else:
        out=[]
        for i in range(step,Max+1):
            tmp=recursolution(size-i,Max-1,i)
            for each in tmp:
                out.append((i,each))
        return out

print(solution(15))

# else:
#         out=[]
#         for j in range(3,Max):    
#             for i in range(step,Max+1):
#                 tmp=recursolution(size-i,j-1,i)
#                 for each in tmp:
#                     out.append((i,each))
#         # if step>Max:
#         #     out.append((step,step+1,size-step-1))
#         return out


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

# else:
#         out=[]
#         for j in range(3,Max):    
#             for i in range(step,Max+1):
#                 # count+=recursolution(size-i,j-1,i)
#                 tmp=recursolution(size-i,j-1,i)
#                 for each in tmp:
#                     out.append((i,each))
#         return  out #count