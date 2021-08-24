
# def origin_return(move_sequence):
#     x_orig = 0
#     y_orig = 0
#     R = x_orig + 1
#     L = x_orig - 1
#     U = y_orig + 1
#     D = y_orig - 1
#     for i in move_sequence:
#         if :
#             rerurn True
#         else:
#             return False



def move(x, y, direction):
    if direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    elif direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1
    return x, y

def is_origin(x, y):
    return x == 0 and y == 0


seq = 'UD'
x = 0
y = 0

for direction in seq:
    x, y =  move(x, y, direction)

print(is_origin(x, y))



