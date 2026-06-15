class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # target - first num = remaining 

        # see if remaining is in the rest of the array

        # if not, move to second num, then target - second num

        # using a dict


        newDict = {}

        for num in range(0, len(nums)): # 0

            remaining = target - nums[num]  # 7 - 3 = 4

            if remaining in newDict:

                return [newDict[remaining], num]   

            else:
                newDict[nums[num]] = num  # 3 = 0
