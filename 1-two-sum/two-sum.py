class Solution: 
    def twoSum(self,nums,target):
        num_dic={}
        for i,num in enumerate(nums):
            if target - num in num_dic:
                return([num_dic[target - num],i])
            num_dic[num]=i
        