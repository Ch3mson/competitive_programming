n = int(input())
MOD = 10**9 + 7

dp = [0]*(n + 1)
dp[0] = 1

for i in range(1, n + 1):
  for j in range(1, 7):
    if j <= i:
      dp[i] = (dp[i] + dp[i-j]) % MOD

print(dp[n])
