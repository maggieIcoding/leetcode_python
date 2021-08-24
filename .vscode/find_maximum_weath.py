
def maximumWealth(accounts):
    global sum_L
    sum_L = 0
    for L in accounts:
        for x in L:
            print(x)
            sum_L += x
            #print(sum_L)



accounts = [[2,8,7],[7,1,3],[1,9,5]]
ret = maximumWealth(accounts)
