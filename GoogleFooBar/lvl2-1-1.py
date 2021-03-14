"""

SEE LVL2-1-2 FOR SOLUTION

"""





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
    if left[0][0]==None:
        tempLeft=0
    else:
        tempLeft=left[0][0]
    if right[0][0]==None:
        tempRight=0
    else:
        tempRight=right[0][0]
    if tempLeft < tempRight:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def appendList(lst1, lst2):
    for each in lst2:
        lst1.append(each)

lst=["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
def solution(elevators):
    #sort elevators by major 
    tupleLst=[]
    for lift in elevators:
        tmp=(int(lift[0]),lift)
        tupleLst.append(tmp)
    firstSort=merge_sort(tupleLst)

    #sort elvators by minor
    tupleLst2=[]
    for lift in firstSort:
        liftDigits=lift[1].split(".")
        if len(liftDigits) >1:
            tmp=(int(liftDigits[1]),lift[1],lift[0])
        else:
            tmp=(None, lift[1], lift[0])
        tupleLst2.append(tmp)
    #sublists sorted by first digit
    zeros=[]
    ones=[]
    twos=[]
    threes=[]
    for tpl in tupleLst2:
        if tpl[-1]==0:
            zeros.append(tpl)
        elif tpl[-1]==1:
            ones.append(tpl)
        elif tpl[-1]==2:
            twos.append(tpl)
        else:
            threes.append(tpl)
    secondSort=[]
    if len(zeros)>0:
        zSort=merge_sort(zeros)
        appendList(secondSort,zSort)
    if len(ones)>1:
        oSort=merge_sort(ones)
        appendList(secondSort,oSort)
    if len(twos)>2:
        tSort=merge_sort(twos)
        appendList(secondSort,tSort)
    if len(threes)>3:
        thSort=merge_sort(threes)
        appendList(secondSort,thSort)

    #sort elvators by minor
    tupleLst3=[]
    for lift in secondSort:
        liftDigits=lift[1].split(".")
        if len(liftDigits) >2:
            tmp=(int(liftDigits[2]),lift[1],lift[-1], lift[0])
        else:
            tmp=(None, lift[1], lift[-1], lift[0])
        tupleLst3.append(tmp)
    #sublists sorted by first digit
    # zeros=[]
    # ones=[]
    # twos=[]
    # threes=[]
    # for tpl in tupleLst2:
    #     if tpl[-1]==0:
    #         zeros.append(tpl)
    #     elif tpl[-1]==1:
    #         ones.append(tpl)
    #     elif tpl[-1]==2:
    #         twos.append(tpl)
    #     else:
    #         threes.append(tpl)
    # secondSort=[]
    # if len(zeros)>0:
    #     secondSort.append(merge_sort(zeros))
    # if len(ones)>1:
    #     secondSort.append(merge_sort(ones))
    # if len(twos)>2:
    #     secondSort.append(merge_sort(twos))
    # if len(threes)>3:
    #     secondSort.append(merge_sort(threes))
    return tupleLst3

print(solution(lst))