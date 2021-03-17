# You've been assigned the onerous task of elevator maintenance -- ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 

# Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

# Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

# For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.

def merge_sort(lst,sortby):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid],sortby)
    right = merge_sort(lst[mid:],sortby)
    return merge(left, right,sortby)

def merge(left, right,SortBY):
    if not left:
        return right
    if not right:
        return left
    if left[0][SortBY]==None:
        if (left[0][3]==None and left[0][2]==None):
            tempLeft=-2
        else:
            tempLeft=-1
    else:
        tempLeft=left[0][SortBY]
    if right[0][SortBY]==None:
        if (right[0][3]==None and right[0][2]==None):
            tempRight=-2
        else:
            tempRight=-1
    else:
        tempRight=right[0][SortBY]
    if tempLeft < tempRight:
        return [left[0]] + merge(left[1:], right,SortBY)
    return [right[0]] + merge(left, right[1:],SortBY)

def appendList(lst1, lst2):
    for each in lst2:
        lst1.append(each)

def inList(lst, num):
    for each in lst:
        if num==each:
            return True
    return False

lst=["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]

def solution(elevators):
    firstList=[]#sort elevators by major elements
    for lift in elevators:
        liftDigits=lift.split(".")
        if len(liftDigits) >2:
            tmp=(lift,int(liftDigits[0]),int(liftDigits[1]),int(liftDigits[2]))
        elif len(liftDigits)>1:
            tmp=(lift,int(liftDigits[0]),int(liftDigits[1]),None)
        else:
            tmp=(lift,int(liftDigits[0]),None,None)
        firstList.append(tmp)
    firstSort=merge_sort(firstList,1)

    secondSort=[]#Sort elevators by minor elements
    thirdSort=[]#Sort elements by revision elements
    maxFirstDigit=0
    for lift in firstSort:
        if lift[1]>maxFirstDigit:
            maxFirstDigit=lift[1]
    maxSecondDigit=0
    for lift in firstSort:
        tmp=0
        if lift[2]!=None:
            tmp=lift[2]
        if tmp>maxSecondDigit:
            maxSecondDigit=tmp
    for i in range(0,maxFirstDigit+1):
        secondList=[]
        for lift in firstSort:
            if lift[1]==i:
                secondList.append(lift)
        secondSort=merge_sort(secondList,2)
        print(secondSort)
        
        for i in range(0,maxSecondDigit+1):
            thirdList=[]
            for lift in secondSort:
                used=inList(thirdSort, lift)
                if (lift[2]==i or (lift[2]==None and used==False)):
                    thirdList.append(lift)
            appendList(thirdSort,merge_sort(thirdList,3))
    print(thirdSort)
    out=[]
    for lift in thirdSort:
        out.append(lift[0])
    
    return out
print(solution(lst))