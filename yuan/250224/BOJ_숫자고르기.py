'''
순서대로 줄세우기
-> 최장부분 증가 수열 lis 문제


lis 는 이전 수 +1 이 아니라
이전 dp +1 임

'''
from collections import deque
import sys
input = sys.stdin.readline
# 현재 인덱스, 뽑은 인덱스, 결과 인덱스
def dfs(now,pick,res): # 직전에 뽑은 인덱스,첫줄, 둘째줄
    op = sorted(pick)
    rp = sorted(res)
    if op == rp:
        ans.extend(op[:])
        return
    nxt = arr[now-1]
    if visit[nxt]:
        return
    pick.append(nxt)
    res.append(arr[nxt-1])
    visit[nxt] = 1
    dfs(nxt,pick,res)


n = int(input())
# n 개 숫자
arr = [int(input())for _ in range(n)]
# 0개 안뽑음
pick = deque([]) # 첫쨰줄
res = deque([]) # 둘쨰줄
ans = []

for idx in range(n):
    pick = deque([])  # 첫쨰줄
    res = deque([])  # 둘쨰줄
    pick.append(idx+1)
    res.append(arr[idx])
    visit = [0] * (n + 1)
    visit[idx+1] = 1
    # print('start',idx+1,'-----')
    # print(pick,res)
    dfs(idx+1,pick,res)

s = set(ans)
res = []
for i in s:
    res.append(i)
res_s = sorted(res)
print(len(s))
for i in res_s:
    print(i)