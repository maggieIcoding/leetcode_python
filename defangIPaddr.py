#Input: address = "255.100.50.0"
#Output: "255[.]100[.]50[.]0"

address = "255.100.50.0"

# def defang_IPaddr(address):
#     num_str = address.split('.')
#     join_str = '[.]'
#     new_addr = join_str.join(num_str)
#     print(new_addr)

# defang_IPaddr(address)

def defang_ip(ip_addr):
    ret_str = ''
    for char in ip_addr:
        if char == '.':
            ret_str = ret_str + '[.]'
        else:
            ret_str = ret_str + char
    
    return ret_str

ret = defang_ip(address)

print(ret)