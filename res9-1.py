sum = 0
file_space = True
index = 0
repr_line = []
with open('input9.txt', 'r') as f:
    line = f.readlines()[0][:-1]
    print(line)
    for elem in line:
        if file_space:
            for _ in range(int(elem)):
                repr_line.append(index)
            index += 1
        else:
            for _ in range(int(elem)):
                repr_line.append('.')
        file_space = not file_space


cp_list = repr_line
up_index = len(repr_line) - 1
for i, elem in enumerate(repr_line):
    if i >= up_index:
        break
    if elem != '.':
        continue
    for j in range(up_index, 0, -1):
        if repr_line[j] != '.':
            up_index = j - 1
            cp_list[i], cp_list[j] = cp_list[j], cp_list[i]
            break
    print(i, up_index)

print(cp_list)
for i, elem in enumerate(cp_list):
    if elem == '.':
        break
    sum += i * int(elem)

print(sum)

