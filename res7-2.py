sum = 0

def convert_to_base_3(num):
    result = []
    for i in range(3 ** num):
        val = i
        representation = ""
        for _ in range(num):
            a = val % 3
            representation += str(a)
            val = int((val - a) / 3)
        result.append(representation[::-1])
    return result

with open('input7.txt', 'r') as f:
    for n in f:
        res = int(n.split(":")[0])
        list_of_numbers = [int(x) for x in n.split(":")[1].split()]
        combinations = convert_to_base_3(len(list_of_numbers) - 1)
        for comb in combinations:
            val = list_of_numbers[0]
            for j, num in enumerate(list_of_numbers[1:]):
                if comb[j] == "0":
                    val += num
                elif comb[j] == "1":
                    val *= num
                else:
                    val = int(str(val) + str(num))
            if val == res:
                sum += res
                break
print(sum)
