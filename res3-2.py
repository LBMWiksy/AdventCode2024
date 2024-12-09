sum = 0
enable = True
with open('input3.txt', 'r') as f:
    for n in f:
        index = 0
        while index < len(n) - 6:
            try:
                if n[index:index+4] == "mul(":
                    index += 4
                    a=''
                    while n[index].isdigit():
                        a += n[index]
                        index += 1
                    if n[index] == ',':
                        index += 1
                        b=''
                        while n[index].isdigit():
                            b += n[index]
                            index += 1
                        if n[index] == ')':
                            index += 1
                            if enable:
                                sum += int(a)*int(b)
                elif n[index:index+4] == "do()":
                    enable = True
                    index += 4
                elif n[index:index+7] == "don't()":
                    enable = False
                    index += 7
                else:
                    index += 1
            except Exception as e:
                print(e)
                break
print(sum)