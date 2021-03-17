Memo=[0,0,0]
def recursolution(n):
    if n==3:
        return [[2,1]]
    else:
        tmp=recursolution(n-1)
        Memo.append(len(tmp))
        out=[]
        for lst in tmp:
            tmplst=lst.copy()
            tmplst[0]=tmplst[0]+1
            if out.__contains__(tmplst)==False:
                out.append(tmplst)

            tmplst2=lst.copy()
            if tmplst2[-1]>=2:
                tmplst2.append(1)
                if out.__contains__(tmplst2)==False:
                    out.append(tmplst2)

            for i in range(0,len(lst)):
                tmplst3=lst.copy()
                if lst[i]!=lst[-1]:
                    if lst[i]>lst[i+1]+1:
                        tmplst3[i+1]=tmplst3[i+1]+1
                        if out.__contains__(tmplst3)==False:
                            out.append(tmplst3)
        #print(out)
        return out


def solution(n):
    final=recursolution(n)
    Memo.append(len(final))
    #print(final)
    return len(final)

print(solution(200))
print(Memo)

