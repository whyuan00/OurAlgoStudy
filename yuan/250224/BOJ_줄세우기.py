'''
순서대로 줄세우기
-> 최장부분 증가 수열 lis 문제


lis 는 이전 수 +1 이 아니라
이전 dp +1 임

'''
import sys
input = sys.stdin.readline
#최대 n:200

n = int(input())
arr = [int(input())for _ in range(n)]
dp = [1]*(n) # 모든 수의 최단 길이는 1
for i in range(1,n):
    # dp[i]를 결정하려고 할때
    for j in range(i): # 모든 이전의 dp 값들과 비교
        if arr[i]>arr[j]:
            # 이전까지의 dp값+1과 현재 dp 비교
            dp[i] = max(dp[j]+1,dp[i])

print(n-max(dp))