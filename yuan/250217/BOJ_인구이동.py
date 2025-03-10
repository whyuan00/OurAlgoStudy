'''
bfs로 연합 가능한 국가 체크
not visit 이고 arr의 차이가 l이상 r이하일때


'''

from collections import deque
import sys
input = sys.stdin.readline
def bfs(q,total,num,s): # q, 인구수, 국가수,이동좌표
    global check
    while q:
        x,y = q.popleft()
        # print('현위치',x,y)
        for k in range(4):
            nx,ny = x+dx[k],y+dy[k]
            # print(nx,ny, visit[nx][ny],'n',n,l,abs(arr[nx][ny] - arr[x][y]),r)
            if 0<= nx<n and 0<=ny<n and not visit[nx][ny]:
                if l<= abs(arr[nx][ny] - arr[x][y]) <=r:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    s.append((nx,ny))
                    total+=arr[nx][ny]
                    num+=1
                    check = True
    # print(total,num)
    # print(total//num)
    return(s,total//num)

n, l, r = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0
dx,dy = [1,-1,0,0],[0,0,1,-1]

# 한번 돌기
while True:
    check = False
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                # print("시작점",i,j,arr[i][j])
                visit[i][j] = 1
                q = deque([(i,j)])
                s = deque([(i,j)])
                total = arr[i][j]  # 인구수
                num = 1  # 국가수
                s, num = bfs(q,total,num,s)

                while s:
                    m1,m2 = s.popleft()
                    arr[m1][m2] = num # 바꿔주기

                # for cc in arr:
                #     print(cc)

    if not check:
        print(answer)
        exit()
    answer+=1
