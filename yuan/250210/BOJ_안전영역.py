"""
* 경우의 수 찾을 때 "모든수" 찾았는지 꼭 체크

n이하의 지점은 물에 잠기고
물에 안잠기는 부분의 개수 구하기

n,n돌면서
현위치 방문 안했으면 q돌기

"""

from collections import deque


def bfs(q, cnt, h, visit):
    while q:
        (
            x,
            y,
        ) = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and arr[nx][ny] >= h:
                visit[nx][ny] = cnt
                q.append((nx, ny))
    return


def check(h):
    global maxv
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and arr[i][j] >= h:
                # print(arr[i][j], cnt + 1)
                visit[i][j] = cnt + 1
                q = deque([(i, j)])
                bfs(q, cnt + 1, h, visit)
                cnt += 1
    # print(cnt)
    # for i in visit:
    #     print(i)
    if cnt > maxv:
        maxv = cnt


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
maxh = 0
maxv = 0
for i in arr:
    if max(i) > maxh:
        maxh = max(i)
for h in range(maxh + 1):
    check(h)
print(maxv)
