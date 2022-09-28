#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start




class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True for i in range(n)]
        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i * i
                while j < n:
                    isPrime[j] = False
                    j += i
                i += 1
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count


        
# @lc code=end

