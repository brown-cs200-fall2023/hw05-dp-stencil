def edit_distance_fwd(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]            
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    
                                   dp[i][j-1],    
                                   dp[i-1][j-1])  

    return dp[m][n]

# ----------------------------------------------------------

def edit_distance_bwd(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # ... [FILL IN with what this section of the code is for]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i < m or j < n:
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]          # [FILL IN what this line means wrt problem]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1],   # [FILL IN what this line means wrt problem]
                                       dp[i+1][j],   # [FILL IN what this line means wrt problem]
                                       dp[i+1][j+1]) # [FILL IN what this line means wrt problem]

    return dp[0][0]