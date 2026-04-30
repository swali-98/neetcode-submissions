class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initializing a set so while adding each element of the list 
        # if the add method returns false it means it is duplicated 
        duplicate_set = set()
        for i in nums:
            if i in duplicate_set:
                return True
            duplicate_set.add(i)    
        return False

        