sum = 0
sum_valid = 0
rules_dict = {}
list_of_reports = []
with open('input5.txt', 'r') as f:
    for n in f:
        line = n[:-1]
        if "|" in line:
            a = [int(x) for x in line.split("|")]
            if a[0] not in rules_dict:
                rules_dict[a[0]] = {"before": [], "after": []}
            rules_dict[a[0]]["before"].append(a[1])
            if a[1] not in rules_dict:
                rules_dict[a[1]] = {"before": [], "after": []}
            rules_dict[a[1]]["after"].append(a[0])
        elif "," in line:
            list_of_reports.append([int(x) for x in line.split(",")])

for report in list_of_reports:
    valid = True
    for val, fval in zip(report[:-1], report[1:]):
        if fval not in rules_dict[val]["before"]:
            valid = False
            break
    if not valid:
        new_report = []
        no_list = report.copy()
        while no_list != []:
            list_test = no_list.copy()
            val_to_check = list_test[0]
            for val in list_test[1:]:
                if val in rules_dict[val_to_check]["after"]:
                    val_to_check = val
            no_list.remove(val_to_check)
            new_report.append(val_to_check)
        sum += new_report[len(new_report)//2]

print(sum_valid)
print(len(list_of_reports))
print(sum)