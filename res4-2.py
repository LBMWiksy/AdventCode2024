sum = 0
with open('input4.txt', 'r') as f:
    full_array = f.readlines()

for i, lines in enumerate(full_array[1:-1]):
    for j, c in enumerate(lines[1:-1]):
        if c == 'A':
            if full_array[i][j] == 'M' and full_array[i+2][j] == 'M' and full_array[i][j+2] == 'S' and full_array[i+2][j+2] == 'S':
                sum += 1
            if full_array[i][j] == 'S' and full_array[i+2][j] == 'M' and full_array[i][j+2] == 'S' and full_array[i+2][j+2] == 'M':
                sum += 1
            if full_array[i][j] == 'S' and full_array[i+2][j] == 'S' and full_array[i][j+2] == 'M' and full_array[i+2][j+2] == 'M':
                sum += 1
            if full_array[i][j] == 'M' and full_array[i+2][j] == 'S' and full_array[i][j+2] == 'M' and full_array[i+2][j+2] == 'S':
                sum += 1
print(sum)