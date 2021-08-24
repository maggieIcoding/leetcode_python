#Input: left = 1, right = 22
#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#1 <= left <= right <= 10000


def is_self_div(num):
    str_num = str(num)
    for char in str_num:
        if int(char) == 0:
            return False
        if num % int(char) != 0:
            return False
    return True

def search_self_div_nums(start, end):
    ret = []
    for i in range(start, end+1):
        if is_self_div(i):
            ret.append(i)

    return ret


print(search_self_div_nums(1, 22))



# def self_dividing_num(input):
#     ret_num = []
#     for num in input:
#         for d in str(num):
#             if d == 0:
#                 pass   
#             else:
#                 if num % int(d) == 0:
#                     ret_num.append(num)
#                 else:
#                     pass

    # return ret_num

# input = range(1, 10001)
# ret = self_dividing_num(input)
# print(ret)