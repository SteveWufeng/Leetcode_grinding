# problem 278
# The isBadVersion API is already defined for you.
def isBadVersion(version: int, bad):
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int, badver):
        # start searching from middle
        index = n//2
        high = n
        low = 1
        # surround in while loop
        while (True):
            # if the middle is not a bad version, increment index
            previousBad = isBadVersion(index-1, badver)
            bad = isBadVersion(index, badver)
        
            if (not previousBad and bad):
                return index
            if (not bad):
                index += scope//2
            # else if is a bad version, decrement index
            elif bad:
                index -= scope//2

if __name__ == '__main__':
    solve = Solution()
    n =   2126753390
    badVer = 1702766719
    x = solve.firstBadVersion(n, badVer)
    print(x)