class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    rtype = [i, j]
                    return rtype
					
					



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range (len(nums)):
            if not nums[i] in dic:
                dic[nums[i]] = i
            if (target-nums[i] in dic and dic[target-nums[i]] != i):
                if i < dic[target-nums[i]]:
                    rtype = [i,dic[target-nums[i]]]
                else:
                    rtype = [dic[target-nums[i]],i]
                return rtype					