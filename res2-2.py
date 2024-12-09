sum = 0
with open('input2.txt', 'r') as f:
    for line in f:
        list_of_lists = []
        list_of_reports = line.split()
        list_of_reports = [int(x) for x in list_of_reports]
        for i in range(len(list_of_reports)):
            list_of_lists.append(list_of_reports[:i] + list_of_reports[i + 1:])
        final_flag = False
        for n in list_of_lists:
            if len(n) == 1:
                final_flag = True
            elif n[0] < n[1]:
                flag = False
                for ind in range(len(n) - 1):
                    if n[ind] >= n[ind + 1] or n[ind] + 3 < n[ind + 1]:
                        flag = True
                        break
                if not flag:
                    final_flag = True
            elif n[0] > n[1]:
                flag = False
                for ind in range(len(n) - 1):
                    if n[ind] <= n[ind + 1] or n[ind] > n[ind + 1] + 3:
                        flag = True
                        break
                if not flag:
                    final_flag = True
            if final_flag:
                sum += 1
                break
print(sum)