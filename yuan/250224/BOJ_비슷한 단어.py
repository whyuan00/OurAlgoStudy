'''
시간 줄이는 방법 계속 염두에두기...
'''
import sys
input = sys.stdin.readline

def check(w1, w2):
    global maxv
    # 접두사의 최대 길이 구하기
    p1,p2,cnt = 0,0,0
    n1 = len(w1)
    n2 = len(w2)
    if n1<=maxv or n2<=maxv:
        return 0
    while p1<n1 and p2<n2:
        if w1[p1] == w2[p2]:
            cnt+=1
            p1+=1
            p2+=1
        else:
            break
    return cnt

n = int(input())
words = [input().rstrip() for _ in range(n)]

maxv = 0
w1 = []
w2 = []
for i in range(n):
    for j in range(i+1,n):
        v = check(words[i],words[j])
        if v > maxv:
            maxv = v
            w1 = words[i]
            w2 = words[j]
print(''.join(w1))
print(''.join(w2))