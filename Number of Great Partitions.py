class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        total = sum(nums)
        n = len(nums)

        # If total sum < 2k, impossible
        if total < 2 * k:
            return 0

        # dp[s] = number of subsets with sum s
        dp = [0] * k
        dp[0] = 1

        for num in nums:
            for s in range(k - 1, num - 1, -1):
                dp[s] = (dp[s] + dp[s - num]) % MOD

        # count subsets with sum < k
        bad = sum(dp) % MOD

        # total partitions = 2^n
        total_partitions = pow(2, n, MOD)

        # remove bad ones
        answer = (total_partitions - 2 * bad) % MOD
        return answer