class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # the best way is a dict

        newDict = {}

        for num in nums:

            if num in newDict:
                newDict[num] += 1

            else:
                newDict[num] = 0

            maxCount = max(newDict.values()) # this gives the largest count

        for key, value in newDict.items():
            if value == maxCount:
                return key