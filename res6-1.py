import numpy as np

sum = 0
rotation = np.pi / 2
with open('input6.txt', 'r') as f:
    map = f.read().splitlines()
f.close()

for y, lines in enumerate(map):
    for x, char in enumerate(lines):
        if char == '^':
            print("init")
            i, j = x, y
            dx = int(np.cos(rotation))
            dy = - int(np.sin(rotation))
            map[j] = map[j][:i] + "X" + map[j][i + 1:]
            sum += 1
            break
        
while i + dx >= 0 and i + dx <= len(map[0]) - 1 and j + dy >= 0 and j + dy <= len(map) - 1:
    if map[j + dy][i + dx] == "#":
        rotation -= np.pi / 2
        dx = int(np.cos(rotation))
        dy = - int(np.sin(rotation))
    else:
        if map[j + dy][i + dx] == ".":
            map[j + dy] = map[j + dy][:i + dx] + "X" + map[j + dy][i + dx + 1:]
            sum += 1
        i += dx
        j += dy
print(sum)