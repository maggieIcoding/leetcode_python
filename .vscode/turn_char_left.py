
# abcdefg
# 输出: "cdefgab"

    # turned_part = ''
    # left_part = s[k:]
    # for i in range(k):
    #     turned_part += s[i]
    #     #print(turned_part)
    #     new_str = left_part + turned_part
    #     print(new_str)

def turn_char_left(s, k):
    ret_a = ""
    ret_b = ""
    new_str = ""
    inx = 0
    for c in s:
        inx += 1
        if inx > k:
            ret_b += c
        else:
            ret_a += c
    new_str = ret_b + ret_a
    return new_str

s = "abcdefg"
k = 2
print(turn_char_left(s, k))

