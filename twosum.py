from pip import List

class Solution:        
    # constructor
    __slots__ = ["__nums", "__target"]

    def __init__ (self, nums, target):
        # state        
        self.__nums = nums
        self.__target = target
        
    # method
    def two_sum (self):
        map = {}
        for i in range(0, len(self.__nums)):
            if self.__target - self.__nums[i] in map:
                return [i, map[self.__target-self.__nums[i]]]
            map[nums[i]] = i 
            
        return [] # not found!
    
if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    solution = Solution(nums, 5)
    x = solution.two_sum()
    print(x)