#Input: [3,1,2,4]
#Output: [2,4,3,1]
#The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted

def sort_arrary(input):
    evenNum_list = []
    oddNum_list = []
    for num in input:
        if num % 2 == 0:
            evenNum_list.append(num)
        else:
            oddNum_list.append(num)
    for odd_num in oddNum_list:
        evenNum_list.append(odd_num)
    return evenNum_list
    
input = range(5001)
ret = sort_arrary(input)
print(ret)


