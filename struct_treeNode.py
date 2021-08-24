
def struct_treeNode(root):
    num_list = []
    target_num = range(num_L+1, num_R)
    for num in root:
        if num in target_num:
            num_list.append(num)
    for num in num_list:
        final_num = num_L + num + num_R
    return final_num

root = [10,5,15,3,7,"null",18]
num_L = 7
num_R = 15

ret = struct_treeNode(root)
print(ret)
