sum = 0
with open('input4.txt', 'r') as f:
    full_array = f.readlines()

len_lines = len(full_array[0])
len_cols = len(full_array)
for i, lines in enumerate(full_array):
    enable_ub = i <= len_cols - 4
    enable_bu = i >= 3
    for j, c in enumerate(lines):
        enable_lr = j <= len_lines - 4
        enable_rl = j >= 3
        if c == 'X':
            if enable_ub and full_array[i+1][j] == 'M' and full_array[i+2][j] == 'A' and full_array[i+3][j] == 'S':
                sum += 1
            if enable_ub and enable_lr and full_array[i+1][j+1] == 'M' and full_array[i+2][j+2] == 'A' and full_array[i+3][j+3] == 'S':
                sum += 1
            if enable_lr and full_array[i][j+1] == 'M' and full_array[i][j+2] == 'A' and full_array[i][j+3] == 'S':
                sum += 1
            if enable_lr and enable_bu and full_array[i-1][j+1] == 'M' and full_array[i-2][j+2] == 'A' and full_array[i-3][j+3] == 'S':
                sum += 1
            if enable_bu and full_array[i-1][j] == 'M' and full_array[i-2][j] == 'A' and full_array[i-3][j] == 'S':
                sum += 1
            if enable_bu and enable_rl and full_array[i-1][j-1] == 'M' and full_array[i-2][j-2] == 'A' and full_array[i-3][j-3] == 'S':
                sum += 1
            if enable_rl and full_array[i][j-1] == 'M' and full_array[i][j-2] == 'A' and full_array[i][j-3] == 'S':
                sum += 1
            if enable_rl and enable_ub and full_array[i+1][j-1] == 'M' and full_array[i+2][j-2] == 'A' and full_array[i+3][j-3] == 'S':
                sum += 1
print(sum)

                