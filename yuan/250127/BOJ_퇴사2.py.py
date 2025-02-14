'''
가방에 돌덩이 넣고 뺼 때
현재 돌멩이 무게가 기록될 필요 없음

ex. n일부터 5일동안 p일하면
 n+5일에는 무조건 n일의 값+p 와 현재값만 비교하면 됨

'''
from collections import defaultdict
import sys
input = sys.stdin.readline
def find_dp(n):
    # 1배열 time 2배열 pay
    dp = [0] * (n+2)
    dp[0]= 0# 0일차

    for i in range(1,n+1): # n 일자 순회
        # 현재 값은 항상 전날과 현재중 큰걸로 갱신
        if dp[i-1]>dp[i]:
            dp[i] = dp[i-1]

        if i in table: # 비교는 현재값과 하기
            numbers = table[i]
            for t,p in numbers:
                if dp[i-t]+p > dp[i]:
                    dp[i] = dp[i-t]+p

    # print(dp)
    return dp[n]

n = int(input())
table = defaultdict(list)
for i in range(n):
    #  i+t 일자에 p 얻을 수 있음
    t,p = map(int, input().split())
    if i+t<=n:
        table[i+t].append((t,p))

res = find_dp(n) # n 일의 최대값 구하기
print(res)