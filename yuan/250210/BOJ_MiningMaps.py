"""


"""

from collections import deque

dict = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}


def bfs(q):
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            edges[now][nxt] = 1
            # print('다음열',graph[now])
            if not visit[nxt]:  # 방문안한노드
                visit[nxt] = 1
                q.append(nxt)
    return


def connect(graph):
    for i in range(26):
        if graph[i] and not visit[i]:
            visit[i] = 1  # 노드 방문
            q = deque([i])
            bfs(q)
            # print(i,'방문')
    return  # net 개수


while True:
    graph = [[] for _ in range(26)]
    visit = [0] * 26
    edges = [[0] * 26 for _ in range(26)]
    try:
        x = input()
        if x and "BEGIN" in x:
            while True:
                y = input()
                # print('y:',y)
                if "END" not in y:
                    arr = list(y.split())
                    n = len(arr)
                    for i in range(1, n):
                        if dict[arr[i]] not in graph[dict[arr[0]]]:
                            graph[dict[arr[0]]].append(dict[arr[i]])
                        if dict[arr[0]] not in graph[dict[arr[i]]]:  # 반대 방향도 추가
                            graph[dict[arr[i]]].append(dict[arr[0]])
                else:
                    # print('start connect')
                    connect(graph)
                    # print(graph)
                    e = 0
                    for i in range(26):
                        for j in range(i + 1, 26):
                            e += edges[i][j]
                    # print(edges)
                    print("NODES", sum(visit), "EDGES", e)
                    break
    except:
        break
