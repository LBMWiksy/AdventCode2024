sum = 0
file_space = True
index = 0
repr_line = []
empty_list = []
disk_list = []
count = 0
with open('input9.txt', 'r') as f:
    line = f.readline()[:-1]
    print(line)
    for i, elem in enumerate(line):
        if i % 2 == 0:
            if int(elem) > 0:
                disk_list.append([count, int(elem), i // 2])
                for _ in range(int(elem)):
                    repr_line.append(index)
                    count += 1
            index += 1
        else:
            if int(elem) > 0:
                empty_list.append([count, int(elem)])
                for _ in range(int(elem)):
                    repr_line.append('.')
                    count += 1
for val in disk_list[::-1]:
    if val[2] > 9980:
        print(val[2], val[1])
        print(repr_line[:100])
        print(empty_list[0], empty_list[1])
    for emp in empty_list:
        if val[1] <= emp[1] and val[0] > emp[0]:
            repr_line[emp[0]: emp[0] + val[1]], repr_line[val[0]: val[0] + val[1]] = repr_line[val[0]: val[0] + val[1]], repr_line[emp[0]: emp[0] + val[1]]
            emp[0] += val[1]
            emp[1] -= val[1]
            break
print(repr_line[:100])
for i, elem in enumerate(repr_line):
    if elem != '.':
        sum += i * int(elem)

print(sum)

