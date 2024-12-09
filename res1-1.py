ll, rl = [], []
sum = 0
with open('input1.txt', 'r') as f:
    for line in f:
        n = line.split()
        ll.append(int(n[0]))
        rl.append(int(n[1]))
rl.sort()
ll.sort()

for el, er in zip(ll, rl):
    sum += abs(el - er)

print(sum)