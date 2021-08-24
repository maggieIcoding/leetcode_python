
def numOfJewelInStone(jewels, stones):
    jewel_list = []
    for i_S in stones:
        if i_S in jewels:
            jewel_list.append(i_S)
    return len(jewel_list)

jewels = "aA"
stones = "aAAbbbb"

ret = numOfJewelInStone(jewels, stones)
print(ret)



