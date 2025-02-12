"""
상하좌우 단계별로 이동하고 싶을떄
q로 visit칸에 넘버링 하면 됨 

1 익/ 0 안익/-1 없
1 주위 여성방향으로 0->1
모든 토마토 익는 최소일수
"""

from collections import deque

import sys

input = sys.stdin.readline


def bfs(arr, q):
    max = -1
    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nz, nx, ny = z + dz[k], x + dx[k], y + dy[k]
            if (
                0 <= nz < h
                and 0 <= nx < n
                and 0 <= ny < m
                and not visit[nz][nx][ny]
                and arr[nz][nx][ny] == 0
            ):
                arr[nz][nx][ny] = 1  # 토마토 익히기
                visit[nz][nx][ny] = visit[z][x][y] + 1
                max = visit[nz][nx][ny]
                q.append((nz, nx, ny))
    return max


# 가로 세로 높이
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = 0
# 상 하 좌 우 위 아래
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, -1, 1]
# 익은 토마토 위치
q = deque([])
# 안익은 토마토 개수
not_t = 0
# 방문 처리
visit = [[[0] * m for _ in range(n)] for _ in range(h)]

for l in range(h):
    for i in range(n):
        for j in range(m):
            if arr[l][i][j] == 0:  # 안익음
                not_t += 1
            elif arr[l][i][j] == 1:  # 익음
                q.append((l, i, j))
                visit[l][i][j] = 1

if not_t == 0:
    print(day)
    exit()
res = bfs(arr, q)

for l in range(h):
    for i in range(n):
        for j in range(m):
            if arr[l][i][j] == 0:
                print(-1)
                exit()
print(res - 1)
# for i in visit:
#     for k in i:
#         print(k)
#     print()
