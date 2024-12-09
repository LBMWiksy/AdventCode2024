sum = 0

def convert_num_to_bin(num):
    return [str(bin(i)[2:].zfill(num)) for i in range(2 ** num)]

with open('input7.txt', 'r') as f:
    for n in f:
        res = int(n.split(":")[0])
        list_of_numbers = [int(x) for x in n.split(":")[1].split()]
        combinations = convert_num_to_bin(len(list_of_numbers) - 1)
        for comb in combinations:
            val = list_of_numbers[0]
            for j, num in enumerate(list_of_numbers[1:]):
                val = val + num if comb[j] == "1" else val * num
            if val == res:
                sum += res
                break
print(sum)