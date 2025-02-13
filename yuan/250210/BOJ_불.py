"""
notted
출구에서 시작하는 경우도 생각해주기

t
다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다.
'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불

불과 상근이 모두 빈공간 이동 (1초)
벽에는 불붙지 않음
상근이는 불난 다음에 이동
출구는 x가 0또는 y가 0 +1초 -> 시작부터 1초로 세면 문제 없음

이동 못하면 IMPOSSIBLE
"""

from collections import deque


def bfs(q):
    while q:
        x, y, v = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != "#":  # 벽 아니어야함
                # 불인경우 사람 위치로 갈수있음 이미 불인 경우만 아니면 됨
                if v == "*" and not visit_f[nx][ny]:
                    visit_f[nx][ny] = -1
                    q.append((nx, ny, v))
                # 나인경우 불과 나 모두 방문 안한곳만 가능
                elif v == "@" and not visit_f[nx][ny] and not visit_m[nx][ny]:
                    visit_m[nx][ny] = visit_m[x][y] + 1
                    if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
                        print(visit_m[nx][ny])
                        return
                    q.append((nx, ny, v))
    # for i in visit_m:
    # print(i)
    print("IMPOSSIBLE")
    return


def find():
    now = ()  # 현위치 @
    q = deque([])  # 불 *
    for i in range(r):
        for j in range(c):
            if arr[i][j] == "@":
                now = (i, j, "@")
                visit_m[i][j] = 1  # 내 위치
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    print(1)
                    return
            elif arr[i][j] == "*":
                visit_f[i][j] = 1  # 불
                q.append((i, j, "*"))
    q.append(now)  # 내 위치는 불뒤로 넣어줌
    bfs(q)


t = int(input())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(t):
    c, r = map(int, input().split())
    visit_f = [[0] * c for _ in range(r)]
    visit_m = [[0] * c for _ in range(r)]
    arr = [list(input()) for _ in range(r)]
    find()
