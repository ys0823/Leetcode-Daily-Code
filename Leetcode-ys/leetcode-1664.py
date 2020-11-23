#-------------------题目链接---------------------
# https://leetcode-cn.com/problems/ways-to-make-a-fair-array/
#-----------------------------------------------
class Solution:
    def waysToMakeFair(self, nums):
        n = len(nums)
        odd = [0] * (n + 1)
        even = [0] * (n + 1)
        for i in range(1, n+1):
            if i & 1 == 1: #奇数
                odd[i] = odd[i -1]
                even[i] = even[i-1] + nums[i-1]
            else:
                odd[i] = odd[i-1] + nums[i-1]
                even[i] = even[i-1]
        res = 0
        for i in range(n):
            reso = odd[i] - odd[0] + even[n] - even[i+1] #前i个数的奇数和+后半部分的新产生的奇数和（其中后半部分的奇数和是通过所有的偶数和even[n]减去i+1的偶数和even[i+1]）
            rese = even[i] - even[0] + odd[n] - odd[i+1]
            if reso == rese:
                res += 1
        return res
