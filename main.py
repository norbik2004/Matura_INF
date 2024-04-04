data = []


with open("bin.txt", "r") as file:
    for line in file:
        data.append(line.strip())

def count_blocks(number):
    block_number = 0
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