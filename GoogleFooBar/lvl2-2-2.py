import itertools

lst = [3,1,4,1,5,9]

def solution(lst):
    permutations=[]
    for i in range(1,len(lst)+1):
        permutations += itertools.permutations(lst,i)

    permuints=[]
    for tation in permutations:
        tmp=""
        for num in tation:
            tmp+=str(num)
        permuints.append(int(tmp))
    div3=[]
    for ints in permuints:
        if ints%3==0:
            div3.append(ints)
    if len(div3)==0:
        return 0
    return max(div3)
print(solution(lst))