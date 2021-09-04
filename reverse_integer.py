# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Input: x = -123
# Output: -321

# def reverse(ran_num):
#     num_str = str(ran_num)
#     num_list = []

#     if num_str[0] == "-":
#         for i in range(len(num_str)-1,0,-1):
#             num_list.append(num_str[i])
#         return "-" + ''.join(num_list)
#     elif num_str[-1] == "0":
#         for i in range(0,len(num_str),-1):
#             num_list.append(num_str[i])
#             return ''.join(num_list)
#     elif num_str[0] != "-":
#         for i in range(len(num_str)-1,-1,-1):
#             num_list.append(num_str[i])
#         return ''.join(num_list)
#     elif ran_num == 0:
#         return 0

# ran_num = 120


def reverse_ps(numb):
    k = 0
    ret = 0
    # (2**32)/10
    for i in range(1, 10**32):
        if numb < 10**i:
            k = i
            break
    for j in range(k-1, -1, -1):
        value = numb//(10**j)
        ret += value*(10**(k-1-j))
        numb = numb - value * 10**j

    
    return ret

def reverse(numb):
    if numb > 2**32-1 or numb < -2**31:
        return 0
    if numb < 0:
        return -reverse_ps(-numb)
    else:
        return reverse_ps(numb)


ran_num = 12099999
ret = reverse(ran_num)
print(ret)