from collections import deque


def find(l, max_weight, truck_weights, q, n):  # q, 들어가는 트럭 대수, 트럭리스트
    i = 0
    time = 0
    now_num = 0  # 들어간 트럭 대수
    now_sum = 0
    while q:
        # print(time,q)
        # 있는 트럭 나오기
        time += 1
        w = q.popleft()
        if w > 0:
            now_sum -= w
            now_num -= 1

        # 트럭 더 들어가야함
        if i < n:
            # 트럭 못들어가는 경우: 최대 대수 초과됐거나 최대 무게가 초과됐거나
            if now_num > l or now_sum + truck_weights[i] > max_weight:
                q.append(0)
                continue
            q.append(truck_weights[i])
            now_sum += truck_weights[i]
            now_num += 1
            i += 1

    return time


def solution(l, max_weight, truck_weights):
    # 올라가는 최대 대수, 최대 무게, 트럭 무게
    # 순서대로 최단시간에 건너야함
    # 2, 10, 	[7,4,5,6]
    # 한대 지나갈때마다 length 초
    n = len(truck_weights)  # 트럭 총 개수
    q = deque([0 for _ in range(l)])  # 다리 길이

    answer = find(l, max_weight, truck_weights, q, n)  # 한개씩 넣어보기

    return answer
