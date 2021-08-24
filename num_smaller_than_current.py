

def smallerNumbersThanCurrent(nums):
    replicate = nums
    output = []
    count = 0
    for i in nums:        
        for j in replicate:
            if i > j:
                count += 1
                    
        output.append(count)
    return output

nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

# 2 <= len(L) <= 500
# 0 <= item <= 100

print(smallerNumbersThanCurrent(nums))


