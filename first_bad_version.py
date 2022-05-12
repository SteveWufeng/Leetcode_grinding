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
            # if the previous one is not bad and the current one is bad
            previousBad = isBadVersion(index-1, badver)
            bad = isBadVersion(index, badver)
            if (not previousBad and bad):
                return index            # then this is the first bad version
            
            # if current index is bad, then first bad version must be lower than this
            if bad == True:
                high = index-2
                index += (high-low)//2
            # else first bad must be higher than this
            else:
                low = index+1
                index = (high-low)//2

if __name__ == '__main__':
    solve = Solution()
    n =   2126753390
    badVer = 1702766719
    x = solve.firstBadVersion(n, badVer)
    print(x)