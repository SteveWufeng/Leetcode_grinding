class Solution:
    def lengthOfLongestSubstring(self, s):
        currentList = []
        longest = 0;
        for i in range(len(s)):
            if s[i] in currentList:
                if (longest < len(currentList)):
                    longest = len(currentList)
                temp = currentList.pop()
                currentList = [temp]
            currentList.append(s[i])
        if (longest < len(currentList)):
            longest = len(currentList)
        return longest
            

if __name__ == "__main__":
    solve = Solution()
    answer = solve.lengthOfLongestSubstring("bbbb")
    print(answer)