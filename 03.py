# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

inp = list(map(int, input('Insert numbrers: ').split()))
print(set(inp))
