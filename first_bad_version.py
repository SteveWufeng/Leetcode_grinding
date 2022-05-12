# problem 278
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # start searching from middle
        index = n
        # surround in while loop
        while (True):
            # if the middle is not a bad version, increment index
            previousBad = isBadVersion(index-1)
            bad = isBadVersion(index)
        
            if (not previousBad and bad):
                return index
            if (not bad):
                index += index//2
            # else if is a bad version, decrement index
            elif bad:
                index -= index//2
        