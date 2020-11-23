#---------------------题目链接-----------------
#https://leetcode-cn.com/problems/smallest-string-with-a-given-numeric-value/
#--------------------------------------------
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        con = k // 25
        sur = k % 25
        return 'a' * (n-con-1) + chr(97 + sur) + 'z' * con