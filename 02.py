# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Insert number: '))
ans = list()
for i in range(N - 1, 1, -1):
    count = 0
    if N % i == 0:
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                count += 1
        if count == 0:
            ans.append(i)
ans.append(1)
ans.reverse()
ans.append(N)
print(f'For number "{N}" simple dividers are: {ans}')
