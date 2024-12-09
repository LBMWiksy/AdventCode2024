ll, rl = [], []
sum = 0
with open('input1.txt', 'r') as f:
    for line in f:
        n = line.split()
        ll.append(int(n[0]))
        rl.append(int(n[1]))
rl.sort()
ll.sort()
len_rl = len(rl)
len_ll = len(ll)
val_index = 0
for el in ll:
    flag = False
    while not flag and el > rl[val_index]:
        val_index += 1
        print(val_index)
        print(len_rl)
        if val_index == len_rl:
            flag = True
        print(flag)
    if flag:
        break
    val_index_temp = val_index
    flag = False
    while not flag and el == rl[val_index_temp]:
        sum += el
        val_index_temp += 1
        if val_index_temp == len_rl:
            flag = True
print("Sum: ")
print(sum)