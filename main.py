def sort(nums):
   for i in range(len(nums)):
       minpos=i
       for j in range(i,6):
        if nums[j]<nums[minpos]:
           minpos=j
           temp=nums[i]
           nums[i]=nums[minpos]
           nums[minpos]=temp


nums=[4,2,6,1,8,7]
sort(nums)
print(nums)