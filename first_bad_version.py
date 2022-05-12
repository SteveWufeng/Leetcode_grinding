# problem 278
# The isBadVersion API is already defined for you.
def isBadVersion(version: int, bad):
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int, bad):
        # start searching from middle
        index = n
        # surround in while loop
        while (True):
            # if the middle is not a bad version, increment index
            previousBad = isBadVersion(index-1, bad)
            bad = isBadVersion(index, bad)
        
            if (not previousBad and bad):
                return index
            if (not bad):
                index += index//2
            # else if is a bad version, decrement index
            elif bad:
                index -= index//2

if __name__ == '__main__':
    solve = Solution()
    x = solve.firstBadVersion(5, 5)
    print(x)