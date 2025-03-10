from collections import deque
"""
문자열 파싱-> 스택으로 할수도 있음

사전순서 문제일때는 그리디 염두에 두기 
1과 0의 사전순서면 min 으로도 가능 

숫자 찾기 메서드: find 와 rfind(뒤에서찾기)

"""
def solution(strs):
    # s 에서 110빼고 st에 넣기
    answer = []

    for sr in strs:
        n = len(sr)
        st = deque([])
        num = 0
        for i in range(n):
            if sr[i] == "0":
                if len(st) >= 2 and st[-1] == "1" and st[-2] == "1":
                    num += 1
                    st.pop()
                    st.pop()
                    continue
            st.append(sr[i])

        # print(st,num)
        sts = "".join(st)
        if num == 0:
            answer.append(sts)
            continue
        # 첫번째 1의 앞에 110 넣거나 마지막 0의 뒤에 넣기
        pos0 = sts.rfind("0") + 1
        res1 = sts[:pos0] + "110" * num + sts[pos0:]

        pos1 = sts.find("1")
        res2 = sts[:pos1] + "110" * num + sts[pos1:]
        # print(res1,res2)
        answer.append(min(res1, res2))

    return answer
