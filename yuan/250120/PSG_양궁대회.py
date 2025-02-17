'''
l,c
암호는 서로다른 l개의 알파벳소문자로 구성
최소 한개 모음 최소 두개 자음
알파벳 순서로 배열

중복없는 c개의 문자중에 l개를 뽑되
1)사전순으로 배열해야함
2)한개모음,두개 자음이어야함

order에서
선택하거나 안하거나 해서 l개 됐을때 stop
이때 한개모음 두개 자음이어야함
'''
import sys
input = sys.stdin.readline

# 현재 인덱스, 선택한 문자열 개수,모음개수,만들고있는암호
def dfs(i,num,cnt,res):
    # print('선택한문자열개수',num,'모음개수:',cnt,res)
    if num == l: # l개만큼 선택한 경우
        if cnt <1 or l-cnt<2: # 모음 자음 개수
            return
        print(res)
        return
    if i == c: # 끝까지 순회시 return
        return
    #선택하기
    alpha = ordered_strs[i]
    if alpha in s: # 모음
        dfs(i+1,num+1,cnt+1,res+alpha)
    else:# 자음
        dfs(i+1,num+1,cnt,res+alpha)
    #선택안하기
    dfs(i+1,num,cnt,res)
    return

l, c = map(int,input().split())
strs = list(input().split())
ordered_strs = sorted(strs)
res = ''
s = set()
s.add('a')
s.add('e')
s.add('i')
s.add('o')
s.add('u')
dfs(0,0,0,res)
