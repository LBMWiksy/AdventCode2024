sum = 0

antennas_dict = {}
single_antinode = []

with open('input8.txt', 'r') as f:
    len_x = len(f.readline()) - 1
    len_y = len(f.readlines()) + 1
    f.seek(0)
    for j, line in enumerate(f):
        line = line[:-1]
        for i, element in enumerate(line):
            if element == '.':
                pass
            elif element not in antennas_dict:
                antennas_dict[element] = [(i, j)]
            else:
                antennas_dict[element].append((i, j))
for key, value in antennas_dict.items():
    list_antennas = value.copy()
    print(key)
    if key == '8':
        print(value)

    for antenna in value:
        list_antennas.pop(0)
        for other_antenna in list_antennas:
            diff = (antenna[0] - other_antenna[0], antenna[1] - other_antenna[1])
            antinode0 = (int(antenna[0] + diff[0]), int(antenna[1] + diff[1]))
            antinode1 = (int(antenna[0] - 2 * diff[0]), int(antenna[1] - 2 * diff[1]))
            if antinode0[0] >= 0 and antinode0[0] < len_x and antinode0[1] >= 0 and antinode0[1] < len_y:
                if antinode0 not in single_antinode:
                    single_antinode.append(antinode0)
                    sum += 1
            if antinode1[0] >= 0 and antinode1[0] < len_x and antinode1[1] >= 0 and antinode1[1] < len_y:
                if antinode1 not in single_antinode:
                    single_antinode.append(antinode1)
                    sum += 1
print(sum)