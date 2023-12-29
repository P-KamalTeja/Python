def climbStairs(n: int) -> int:
    def dp(n, cache):
        if n not in cache:
            cache[n] = dp(n - 1, cache) + dp(n - 2, cache)
        #print(cache[n])
        return cache[n]

    print(dp(n, {1: 1, 2: 2}))


climbStairs(5)
