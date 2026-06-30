class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # it says in-place, meaning I need to modify the existing array instead of creating a new one

        # first I think I should get the k value

        k = 0
        length = len(nums)
        iteration = 0

        for num in nums: 
            if num != val:
                k += 1

        for num in range(0,length):
            if nums[iteration] == val:
                nums.remove(val) # now nums wont have the value 
                nums.append("_")  
            else:
                iteration += 1


        return k
        return nums