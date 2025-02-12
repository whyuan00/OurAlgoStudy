def cal(path, ans):
    # print(path)
    s = 0
    res = path.split("+")
    # print(res)
    for r in res:
        if "-" in r:
            m = r.split("-")
            s += int(m[0])
            for i in m[1:]:
                s -= int(i)
        else:
            s += int(r)
    if s == 0:
        print(ans)
    return


def dfs(i, n, path, ans):
    if i == n:
        cal(path, ans)
        return
    #
    dfs(i + 1, n, path + "" + str(i + 1), ans + " " + str(i + 1))
    # +
    dfs(i + 1, n, path + "+" + str(i + 1), ans + "+" + str(i + 1))
    # -
    dfs(i + 1, n, path + "-" + str(i + 1), ans + "-" + str(i + 1))


t = int(input())
for _ in range(t):
    n = int(input())
    path = "1"
    ans = "1"
    dfs(1, n, path, ans)
    print()
