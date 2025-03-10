'''
딕셔너리 sorted 하면 리스트로 바뀜

value 기준으로 sort하기:
sorted(dict, key = lamba x: dict[x])

'''

from collections import Counter

def solution(n, stages):
    counter = Counter(stages)
    # print(counter)
    dic = dict()
    total = len(stages)  # 전체 사람 수
    for i in range(1, n + 1):  # 스테이지 개수 확인
        if i in counter:
            dic[i] = float(counter[i] / total)
            total -= counter[i]  # 전체수에서 뺴주기
        else:
            dic[i] = 0
    answer = sorted(dic, key=lambda x: dic[x], reverse=True)
    return answer
