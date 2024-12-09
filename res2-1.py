sum = 0
with open('input2.txt', 'r') as f:
    for line in f:
        n = line.split()
        n = [int(x) for x in n]
        if len(n) == 1:
            sum += 1
        elif n[0] < n[1]:
            flag = False
            for ind in range(len(n) - 1):
                if n[ind] >= n[ind + 1] or n[ind] + 3 < n[ind + 1]:
                    flag = True
                    break
            if not flag:
                sum += 1
        elif n[0] > n[1]:
            flag = False
            for ind in range(len(n) - 1):
                if n[ind] <= n[ind + 1] or n[ind] > n[ind + 1] + 3:
                    flag = True
                    break
            if not flag:
                sum += 1
print(sum)