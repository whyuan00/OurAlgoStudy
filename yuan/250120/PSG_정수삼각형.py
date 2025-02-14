def solution(triangle):
    n = len(triangle) 
    dp = [[0]*i for i in range(1,n+1)]
    # print(dp)
    dp[0][0] = triangle[0][0] 
    for i in range(1,n): # i행 j열 
        for j in range(i+1):
            # l, r = dp[i-1][j-1], dp[i-1],dp[j]
            l,r = 0,0
            if 0<=j-1<=i-1:
                l = dp[i-1][j-1]
                # print('l좌표:',i-1,j-1,l)
            if 0<=j<=i-1:
                r = dp[i-1][j]
                # print('r좌표:',i-1,j,r)
                
            dp[i][j] = max(r+triangle[i][j], l+triangle[i][j])
            
    # print(dp)     
    return max(dp[-1])
    
