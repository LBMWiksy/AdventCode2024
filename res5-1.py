sum = 0
rules_dict = {}
list_of_reports = []
with open('input5.txt', 'r') as f:
    for n in f:
        line = n[:-1]
        if "|" in line:
            a = [int(x) for x in line.split("|")]
            if a[0] not in rules_dict:
                rules_dict[a[0]] = []
            rules_dict[a[0]].append(a[1])
        elif "," in line:
            list_of_reports.append([int(x) for x in line.split(",")])
for report in list_of_reports:
    valid = True
    for val, fval in zip(report[:-1], report[1:]):
        if val in rules_dict and fval in rules_dict:
            if fval not in rules_dict[val]:
                valid = False
                break
    if valid:
        sum += report[len(report)//2]
print(sum)