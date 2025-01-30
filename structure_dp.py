def min_coins(target, coins):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        print(coin, target + 1)
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[target] if dp[target] != float('inf') else -1

coins = [500, 400, 100]
target = 800
print(min_coins(target, coins))  # Output: 2 (400 + 400)