# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

def defang_IP(input_IP):
    new_IP = []
    for x in input_IP:
        if x != '.':
            new_IP.append(x)
        else:
            x = '[.]'
            new_IP.append(x)
        new_IP_address = ''.join(new_IP)
    print(new_IP_address)

input_IP = "255.100.50.0"
defang_IP(input_IP)