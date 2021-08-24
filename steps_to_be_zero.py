# class Solution(object):
#     def __init__(self, num, dev_num):
#         self.num = num
#         self.dev_num = dev_num

#     def numberOfSteps (self, num):
#         self.devision = []
#         self.subtractor = []
#         self.count = 0
#         if self.num % 2 == 0:   # if num is even
#             self.dev_num == num / 2
#             if self.dev_num != 0:
#                 self.devision.append(self.dev_num)
#             else:
#                 pass
#         elif num % 2 == 1:
#             min_num = num - 1
#             if min_num != 0:
#                 self.subtractor.append(min_num)
#             else:
#                 pass
def number_of_step(num):
    divisor_L = []
    subtractor_L = []
    divisor = ''
    subtractor = ''
    if num % 2 == 0:
        int(divisor) == num / 2
        if int(divisor) % 2 == 0:
            divisor_L.append(int(divisor))
        elif divisor % 2 != 0:
            subtractor = int(divisor) - 1
            subtractor_L.append(int(subtractor))
    else:
        divisor = num - 1
        divisor_L.append(divisor/2)
    return divisor_L
    #return subtractor_L

ret = number_of_step(14)

print(ret)


