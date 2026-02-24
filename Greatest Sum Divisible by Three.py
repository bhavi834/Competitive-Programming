class Solution:
    def maxSumDivThree(self, nums):
        total = sum(nums)

        ones = []
        twos = []

        for num in nums:
            if num % 3 == 1:
                ones.append(num)
            elif num % 3 == 2:
                twos.append(num)

        ones.sort()
        twos.sort()

        if total % 3 == 0:
            return total

        if total % 3 == 1:
            remove1 = ones[0] if len(ones) >= 1 else float('inf')
            remove2 = twos[0] + twos[1] if len(twos) >= 2 else float('inf')
            return total - min(remove1, remove2)

        if total % 3 == 2:
            remove1 = twos[0] if len(twos) >= 1 else float('inf')
            remove2 = ones[0] + ones[1] if len(ones) >= 2 else float('inf')
            return total - min(remove1, remove2)