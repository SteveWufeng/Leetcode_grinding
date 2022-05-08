from pip import main


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentList = []
        longest = 0;
        for ch in s:
            if ch in currentList:
                if (longest < len(currentList)):
                    longest = len(currentList)
                currentList = []
            currentList.append(ch)
        return longest
            

if __name__ == "__main__":
    solve = Solution()
    answer = solve.lengthOfLongestSubstring("abcabcbb")
    print(answer)