class Solution:
    def lengthOfLongestSubstring(self, s):
        currentList = []
        longest = 0;
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in currentList:
                    if (longest < len(currentList)):
                        longest = len(currentList)
                    currentList = []
                currentList.append(s[j])
            if (longest < len(currentList)):
                longest = len(currentList)
            temp = currentList.pop()
            if (temp != s[j]):
                currentList = [temp]
            else:
                currentList = []
        return longest
            

if __name__ == "__main__":
    solve = Solution()
    answer = solve.lengthOfLongestSubstring("bbbbb")
    print(answer)