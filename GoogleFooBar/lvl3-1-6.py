# Reference=[0,0,0]
# for i in range(3,201):
#     Reference.append(solution(i))
#     print(Reference[i])
# print(Reference)
correctValues=[0, 0, 0, 1, 1, 2, 3, 4, 5, 7, 9, 11, 14, 17, 21, 26, 31, 37, 45, 53, 63, 75, 88, 103, 121, 141, 164, 191, 221, 255, 295, 339, 389, 447, 511, 584, 667, 759, 863, 981, 1112, 1259, 1425, 1609, 1815, 2047, 2303, 2589, 2909, 3263, 3657, 4096, 4581, 5119, 5717, 6377, 7107, 7916, 8807, 9791, 10879, 12075, 13393, 14847, 16443, 18199, 20131, 22249, 24575, 27129, 29926, 32991, 36351, 40025, 44045, 48445, 53249, 58498, 64233, 70487, 77311, 84755, 92863, 101697, 111321, 121791, 133183, 145577, 159045, 173681, 189585, 206847, 225584, 245919, 267967, 291873, 317787, 345855, 376255, 409173, 444792, 483329, 525015, 570077, 618783, 671417, 728259, 789639, 855905, 927405, 1004543, 1087743, 1177437, 1274117, 1378303, 1490527, 1611387, 1741520, 1881577, 2032289, 2194431, 2368799, 2556283, 2757825, 2974399, 3207085, 3457026, 3725409, 4013543, 4322815, 4654669, 5010687, 5392549, 5802007, 6240973, 6711479, 7215643, 7755775, 8334325, 8953855, 9617149, 10327155, 11086967, 11899933, 12769601, 13699698, 14694243, 15757501, 16893951, 18108417, 19406015, 20792119, 22272511, 23853317, 25540981, 27342420, 29264959, 31316313, 33504745, 35839007, 38328319, 40982539, 43812109, 46828031, 50042055, 53466623, 57114843, 61000703, 65139007, 69545357, 74236383, 79229675, 84543781, 90198445, 96214549, 102614113, 109420548, 116658615, 124354421, 132535701, 141231779, 150473567, 160293887, 170727423, 181810743, 193582641, 206084095, 219358314, 233451097, 248410815, 264288461, 281138047, 299016607, 317984255, 338104629, 359444903, 382075867, 406072421, 431513601, 458482687, 487067745]


from functools import lru_cache
import sys
import time
sys.setrecursionlimit(10000)

Memo=dict()
#Results=dict()

def solution(n):
    # if n in Results:
    #     return Results[n]
    count=0
    for y in range(1,n):
        #print(Memo)
        if (n,y) in Memo:
            count+= Memo[(n,y)]
        else:
            Memo[(n,y)]=CountStairCases(n,y)
            count+=Memo[(n,y)]
    print(Memo)
    return count-1
    # Results[n]=count-1    
    # return Results[n]

def CountStairCases(X,Y):
    print(Memo)
    if Y<=0 or X<=0:
        return 0
    elif X==Y and X==1:
        return 1
    elif X==Y and X>1:
        return 0
    else:
        if Memo[(X-Y,Y)]:
            if Memo[(X-Y,Y-1)]:
                return Memo[(X-Y,Y)]+Memo[(X-Y,Y-1)]
            else:
                Memo[(X-Y,Y-1)]=CountStairCases(X-Y,Y-1)
                return Memo[(X-Y,Y)]+Memo[(X-Y,Y-1)]
        elif Memo[(X-Y,Y-1)]:
            Memo[(X-Y,Y)]=CountStairCases(X-Y,Y)
            return Memo[(X-Y,Y)]+Memo[(X-Y,Y-1)]
        else:
            Memo[(X-Y,Y)]=CountStairCases(X-Y,Y)
            Memo[(X-Y,Y-1)]=CountStairCases(X-Y,Y-1)
            return Memo[(X-Y,Y)]+Memo[(X-Y,Y-1)]

def solution1(n):
    count=0
    for y in range(1,n):
        # print("this is the end",y)
        count+=CountStairCases(n,y)
        
    return count-1

@lru_cache
def CountStairCases(X,Y):
    # print("recursion:",X,Y)
    if Y<=0 or X<=0:
        return 0
    elif X==Y and X==1:
        # print("this is base case")
        return 1
    elif X==Y and X>1:
        # print("this is bad case")
        return 0
    else:
        return CountStairCases(X-Y,Y) + CountStairCases(X-Y,Y-1)
start=time.time()
print(solution(15))
end=time.time()
print("elapsed=",end-start)
# start=time.time()
# print(solution1(200))
# end=time.time()
# print("elapsed=",end-start)