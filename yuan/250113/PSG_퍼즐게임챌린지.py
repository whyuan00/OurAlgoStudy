'''
이분탐색 조건
0. 전체 순회해서 풀면 시간 엄청 많이걸림 
1. 하한 상한 확실함


'''
def check(level,n,diffs,times,limit):#난이도, limit, level
    time_prev = 0
    total_time = 0
    for i in range(n):
        diff = diffs[i]
        time_cur = times[i] # 이전은 time_prev
        if diff<=level:
            time_solved = time_cur
        else:
            time_solved =  (diff-level)*(time_prev+time_cur) + time_cur 

        total_time += time_solved
        time_prev = time_cur
        if total_time > limit:
            return False 
    return True

def solution(diffs, times, limit):
    n = len(diffs)
    l,h = 1,max(diffs) # 이분탐색 
    while l<=h:
        if l==h:
            break
        now_level = (l+h)//2 
        if check(now_level,n,diffs,times,limit):
            h = now_level
        else:
            l = now_level+1 
        
    answer = h
    return answer