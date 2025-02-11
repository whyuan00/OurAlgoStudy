def find(parent,x):
    if parent[x] != x:
        # 값 '갱신' 이지 dfs 가 아님 
        # return은 딱 한개만 존재해야됨 
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent,i,j):
    ri = find(parent,i)
    rj = find(parent,j)
    # 연결 안된 상태기때문에 연결해줘야함
    if ri!=rj:
        parent[rj] = ri 
    
def solution(n, computers):
    # 부모는 자기 자신으로 기본값 설정 
    parent = [i for i in range(n)] 
    
    # n*n개의 노드 연결을 전부 확인해주기 
    for i in range(n):
        for j in range(n):
            if computers[i][j] ==1:
                # 연결된 컴퓨터면 집합 합치기
                union(parent,i,j) 

    # 부모 노드 구한 상황에서 
    # 다시 find로 네트워크 개수 세기 
    answer = len(set(find(parent,i) for i in range(n)))
            
    return answer