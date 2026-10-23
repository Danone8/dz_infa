def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (s1[i - 1] != s2[j - 1]))

    return dp[m][n]


def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


res = []
i, j = len(a), len(b)
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        res.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
retturn dp[m][n], ''.join(reversed(res))



def lis(a):
    dp = []
    pos = []
    prev = [-1]*len(a)
    for i, x in enumerate(a):
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < x:
                left = mid + 1
            else:
                right = mid
        j = left
        if j>0:
            prev[i] = pos[j-1]
        if j == len(dp):
            dp.append(x)
            pos.append(i)
        else:
            dp[j] = x
            pos[j] = i

    ans = []
    if pos:
        k = pos[-1]
        while k >= 0:
            ans.append(a[k])
            k = prev[k]

    return len(dp), ans[::-1]

#посмотреть алгоритм за n**2

#в задааче с рюкзаком 1 прелмет