'''
Counter 는 숫자 세주는 dict 임 dict[x]+=1 대신해줌
combinations 와 permutations 주의
순열은 중복 포함한 값임

'''
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        combs = []
        for order in orders:
            x = [ ''.join(sorted(combo)) for combo in combinations(order,c)]
            combs.extend(x)
    
        counter = Counter(combs)
        if counter and max(counter.values()) >1:
            maxv = max(counter.values())
            answer.extend([k for k,v in counter.items() if v ==maxv])
    
    return sorted(answer)