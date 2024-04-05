data = []


with open("bin.txt", "r") as file:
    for line in file:
        data.append(line.strip())

def count_blocks(number):
    block_number = 1
    prev_char = ''
    for char in number:
        if block_number == 0:
            block_number = 1
            prev_char = char
        else:
            if prev_char != char:
                block_number += 1
                prev_char = char
    return block_number


final_answer = 0
for number in data:
    answer = count_blocks(number)
    if answer <= 2:
        final_answer += 1
print(final_answer)

format(int(data[0], 2), "d")


def get_highest_block(data_array):
    highest_block = 0
    for integer in data_array:
        integer = int(integer, 2)
        if integer > highest_block:
            highest_block = integer
    return bin(highest_block)[2:]


print(get_highest_block(data))

numerek = "1111011"
numerek = format(int(numerek, 2), "d")
print(numerek)
