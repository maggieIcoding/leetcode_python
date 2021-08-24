#Tips: 找一个无关的变量，把相关的变量和这个无关的变量建立联系

candies = [2,3,5,1,3] 
extraCandies = 3
# Output = [true,true,true,false,true] 

def find_maximum(L): #找出list L里最大值
    if L:    # if the list is not blank
        a = L[0]
        for item in L:
            if item > a:
                a = item
        return a
def find_minimum(L): #找出list L里最小值
    a = L[0]
    for item in L:
        if item < a:
            a = item
    return a
#print(find_minimum(candies))
def find_arv_number(L):  #找出list L的平均数
    n = len(L)
    a = 0   # a是一个无关的变量，用a=0和遍历列表里的每个数建立联系
    for item in L:
        a += item  #等于表达式(a = a + item) 求列表L所有值之和
    avg = a/n

    return avg
#print(find_arv_number(candies))        

def find_num_close_to_arv_number(L, avg): #找出list L中最接近平均数的值
    a = L[0]
    for item in L:
        if item - avg < a:
            a = item
    return a

print(find_num_close_to_arv_number(candies, 2.8))

def get_greatest_number(maximum, extraCandies, candy_list): #比较 extraCandies与list中的每个值
    bool_list = []
    for item in candy_list:
        bool_list.append(item+extraCandies>maximum) 
    return bool_list

#print(get_greatest_number(find_maximum(candies),extraCandies,candies))
