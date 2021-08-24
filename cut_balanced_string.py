
# def balanced_str(orig_str):
#     bal_str = ''
#     r_count = 0
#     l_count = 0
#     for char in orig_str:
#         if char == 'R':
#             r_count += 1
#         else:
#             l_count += 1
#     if r_count == l_count:

def balanced_str(origin_str):
    ret = []
    
    scan_count = 0     #计算越过balance线
    flag = ''          #如果第一个字符是R，遍历时判断是否应该加1还是减1
    tmp = ''           #最后符合要求的字符串
    for char in origin_str:
        if scan_count == 0:
            flag = char
            scan_count += 1
            tmp = char
        else:
            tmp += char
            if char == flag:
                scan_count += 1
            else:
                scan_count -= 1
                if scan_count == 0:
                    ret.append(tmp)

    return ret


print(balanced_str("RLLLLRRRLR"))