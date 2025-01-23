def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()

        for num in nums:
            numset.add(num)

        if len(nums) == len(numset):
            return False
        else:
            return True