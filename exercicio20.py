num = []

for i in range(3):
    num.append(int(input("Digite um valor inteiro: ")))

num_len = len(num)
for u in range(num_len - 1):
    for i in range(num_len - 1):
        if num[i] > num[i + 1]:
            aux = num[i]
            num[i] = num[i + 1]
            num[i + 1] = aux

print(num[num_len-1])
