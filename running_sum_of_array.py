
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

def runningSum(num_list):
    inx = 0
    new_num = 0
    new_list = []
    for num in num_list:
        inx += 1
        new_num += num
        new_list.append(new_num)
    return new_list

num_list = [1,2,3,4]
ret = runningSum(num_list)
print(ret)


    