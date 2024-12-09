import numpy as np

sum = 0
rotation = np.pi / 2
with open('test2.txt', 'r') as f:
    map = f.read().splitlines()
f.close()

for y, lines in enumerate(map):
    for x, char in enumerate(lines):
        if char == '^':
            i, j = x, y
            dx = int(np.cos(rotation))
            dy = - int(np.sin(rotation))
            break

list_last_turns = [[], [], [], []]
valid_obstacles = []
turns = 0
while i + dx >= 0 and i + dx <= len(map[0]) - 1 and j + dy >= 0 and j + dy <= len(map) - 1:
    if map[j + dy][i + dx] == "#":
        last_turn = [i + dx, j + dy]
        list_last_turns[turns % 4].append(last_turn)
        rotation -= np.pi / 2
        dx = int(np.cos(rotation))
        dy = - int(np.sin(rotation))
        turns += 1
        for pos in list_last_turns[(turns + 1) % 4]:
            flag_obstacle = False
            x_dir = dx + int(np.cos(rotation - np.pi / 2))
            y_dir = dy - int(np.sin(rotation - np.pi / 2))
            if (i < pos[0] and x_dir < 0) or (i > pos[0] and x_dir > 0) or (j < pos[1] and y_dir < 0) or (j > pos[1] and y_dir > 0):
                continue
            # print("Whoaaa")
            # print(dx, dy)
            # print(int(np.cos(rotation - np.pi / 2)), -int(np.sin(rotation - np.pi / 2)))
            # print(x_dir, y_dir)
            # print(i, j)
            # print(pos)
            len1 = abs(dx) * abs(pos[0] - i) + abs(dy) * abs(pos[1] - j)
            len2 = abs(int(np.cos(rotation - np.pi / 2))) * abs(pos[0] - i) + abs(int(np.sin(rotation - np.pi / 2))) * abs(pos[1] - j)
            # print(len1, len2)
            for k in range(1, len1 + 1):
                # print(i + k * dx, j + k * dy)
                if map[j + k * dy][i + k * dx] == "#":
                    flag_obstacle = True
                    # print("f")
                    break
            for k in range(1, len2 + 1):
                # print(i + k * int(np.cos(rotation - np.pi / 2)) + dx * len1, j - k * int(np.sin(rotation - np.pi / 2)) + dy * len1)
                if map[j - k * int(np.sin(rotation - np.pi / 2))][i + k * int(np.cos(rotation - np.pi / 2))] == "#":
                    flag_obstacle = True
                    # print("f")
                    break
            # print(flag_obstacle)
            # print((i + len1 * dx, j + len1 * dy) not in valid_obstacles)
            if not flag_obstacle and (i + len1 * dx, j + len1 * dy) not in valid_obstacles:
                valid_obstacles.append((i + len1 * dx, j + len1 * dy))
                sum += 1
    else:
        if map[j + dy][i + dx] == ".":
            map[j + dy] = map[j + dy][:i + dx] + "X" + map[j + dy][i + dx + 1:]
        i += dx
        j += dy
f = open('test_show.txt', 'a')
for line in map:
    f.write(line + "\n")
f.close()
print(sum)