"""
0~9까지 비트 연산 기준으로 몇개 다른지 알기
arr 돌면서 각 숫자로 바꿀수 있는 개수가 x,y,.. 일때
x+y+...가 p 개 이하고
xy.. 가 n 이하

"""

dic = {
    0: "1111110",
    1: "0110000",
    2: "1101101",
    3: "1111001",
    4: "0110011",
    5: "1011011",
    6: "1011111",
    7: "1110000",
    8: "1111111",
    9: "1111011",
}


def dfs(i, now, cnt):
    if cnt > p:
        return
    if i == k:
        if 1 <= int(now) <= n:
            # print(now, cnt)
            s.add(now)
        return
    # arr[i]에서 바꿀 수 있는 자리수 바꾸기
    for idx, x in enumerate(numbers[arr[i]]):
        if x > p:
            continue
        dfs(i + 1, now + str(idx), cnt + x)
    # return


# 최대층, 자리수, 반전시키는 최소개수, 현재층
n, k, p, x = map(int, input().split())
arr = [0] * k  # 자리수만큼 만들기

numbers = [[-1] * 10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        numbers[i][j] = sum(1 for p, q in zip(dic[i], dic[j]) if p != q)
# print(numbers)
# [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
#  [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
#  [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
#  [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
#  [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
#  [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
#  [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
#  [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
#  [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
#  [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]
i = 0
while i < k:
    arr[k - 1 - i] = x % 10
    i += 1
    x //= 10
# 현재 확인하는 자리수, 현재 층, 바꾼 개수
s = set()
dfs(0, "", 0)
print(len(s) - 1)
