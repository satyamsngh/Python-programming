def runningSum(self):
     n=len(nums)
     ar=[nums[0]]
     for i in range (1,n):
         nums[i]+=nums[i-1]
         ar.append(nums[i])
     return ar
nums=[1,3,4,5]
print(runningSum(nums))