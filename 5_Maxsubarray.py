# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


def Maxsubarray(nums):
    cmax = nums[0]
    gmax = nums[0]

    for i in range(1,len(nums)):
        cmax = max(nums[i],cmax+nums[i])
        gmax = max(cmax,gmax)

    return gmax

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Maxsubarray(nums))



# to also return the subarray
def maxsub(nums):

    cmax = nums[0]
    gmax = nums[0]

    start = 0
    end = 0
    temp_start = 0

    for i in range(1,len(nums)):

        if nums[i] > cmax+nums[i]:
            cmax = nums[i]
            temp_start = i

        else:
            cmax = cmax+nums[i]

        if cmax > gmax:
            gmax = cmax
            start = temp_start
            end = i

    return gmax , nums[start:end+1]

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxsub(nums))


