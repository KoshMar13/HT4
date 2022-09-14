# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

N = float(input('Insert number: '))
accurInp = float(input('Insert accuracy: '))
accurReal = 0
while accurInp != 1:
    accurInp *= 10
    accurReal += 1

print(round(N, accurReal))
