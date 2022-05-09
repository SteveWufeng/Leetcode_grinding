# problem 3
#https://youtu.be/wiGpQwVHdE0
class Solution:
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        leftIndex = 0
        longestLen = 0
        
        for i in range(len(s)):
            # as long as there is duplicate remove from the left index
            while s[i] in charSet:
                charSet.remove(s[leftIndex])
                leftIndex += 1
            charSet.add(s[i])
            longestLen = max(longestLen, (i - leftIndex+1))
        
        return longestLen

if __name__ == "__main__":
    solve = Solution()
    answer = solve.lengthOfLongestSubstring("bbbbb")
    print(answer)