#-------------------------题目链接----------------
#https://leetcode-cn.com/problems/remove-k-digits/
#博客：https://www.cnblogs.com/yeshengCqupt/p/14057027.html
#-----------------------------------------------
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = [int(i) for i in num]
        stack = list()
        for i in range(0, len(num)):
            if not stack or stack[-1] < num[i]:
                stack.append(num[i])
            else:
                while stack and stack[-1] > num[i] and k != 0:
                    stack.pop()
                    k -= 1
                stack.append(num[i])
        while k != 0:
            stack.pop()
            k -= 1
        res = (''.join(str(i) for i in stack)).lstrip('0')
        if res:
            return res
        else:
            return '0'

s = Solution()
string = '100'
k = 1
res = s.removeKdigits(string, k)
print(res)