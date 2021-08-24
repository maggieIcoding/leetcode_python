nums = [1,2,3,4]
# Output: [2,4,4,4]

#[freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0)

# def decompress_RLE_list(nums):
#     decom_pair = []
#     val_list = []
#     for i in nums:
#         i = 0
#         i += 1
#         freq = nums[2*i]
#         val = nums[2*i+1]
#         decom_pair = {freq : val}
#         val_list.append(decom_pair.values())
#     return val_list

# print(decompress_RLE_list(nums))
def decompress_RLE_list(nums):

    is_freq_flag = True  #设定一个初始值， list[0] 是freq 
    out_put = []
    for num in nums:
        print("flag is {}, num is {}".format(is_freq_flag, num))
        if is_freq_flag:
            is_freq_flag = False
            freq = num
        else:
            is_freq_flag = True
            for _ in range(freq):  #重复 'num' range(freq) 次数
                out_put.append(num)
    return out_put

print(decompress_RLE_list(nums))

