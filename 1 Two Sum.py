'''
Time complexity: O(n​^2​​)
Space complexity:O(1​​)
'''
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
		print "No two sum solution"		//别忘了无解的情况			
					


'''
Time complexity: O(n​​​)
Space complexity:O(n)
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range (len(nums)):
            if (target-nums[i] in dic):
                if i < dic[target-nums[i]]:
                    rtype = [i,dic[target-nums[i]]]
                else:
                    rtype = [dic[target-nums[i]],i]
                return rtype
			if not nums[i] in dic:
                dic[nums[i]] = i
		print "No two sum solution"