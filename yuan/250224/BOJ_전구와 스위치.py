'''
i번 스위치 누르면 앞 본 뒤 세개 반대로 바뀜

어차피 끝까지 확인해야하기때문에
중간에 비교하는 코드 있으면 시간 많이 잡아먹음
# if now == res:
#     if cnt < minv:
#         minv = cnt
#     return
'''

def find(cnt,i,fis,res,check):
    global minv
    now = fis[:]
    while i < n:
        if cnt > minv:
            return
        # if now == res:
        #     if cnt < minv:
        #         minv = cnt
        #     return
        # 이전값이 다름
        if now[i - 1] != res[i - 1]:
            cnt += 1
            now[i - 1] = dic[now[i - 1]]
            now[i] = dic[now[i]]
            if i + 1 < n:
                now[i + 1] = dic[now[i + 1]]
        i += 1
    # print(i, now)
    if now == res:
        if cnt < minv:
            minv = cnt
        return
import sys
input = sys.stdin.readline
n = int(input())
fis = list(input())
res = list(input())
dic = {'1':'0','0':'1'}
minv = 1e9

cnt = 0
i = 1
# 0번 스위치 안누르기
find(cnt,i,fis,res,0)
# 0번 스위치 누르기
cnt = 1
i = 1
fis[i-1] = dic[fis[i-1]]
fis[i] = dic[fis[i]]
find(cnt,i,fis,res,1)
if minv ==1e9:
    print(-1)
else:
    print(minv)