# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def MyStrip(someString):
    someStrMod = someString
    someStrMod = someStrMod.replace('+', ' ')
    someStrMod = someStrMod.replace('-', ' ')
    someStrMod = someStrMod.replace('*x**', ' ')
    someStrMod = someStrMod.replace('*x', ' 1')
    someList = list(someStrMod.split())
    return someList


def polyPairs(someList):
    if len(someList) % 2 == 1:
        someList.append('0')
    print(someList)
    pairs = list()
    while len(someList) != 0:
        pair = list()
        for j in range(2):
            pair.append(int(someList[0]))
            someList.pop(0)
        pairs.append(pair)
    return pairs


def polySum(poly1, poly2):
    for i in range(len(poly1)):
        for j in poly2:
            if poly1[i][1] == j[1]:
                poly1[i] = ((poly1[i][0] + j[0], poly1[i][1]))
                poly2.remove(j)
    ans = poly1 + poly2
    for i in ans:
        if i[0] == 0:
            ans.remove(i)
    ans = sorted(ans, key=lambda elem: elem[1])
    ans.reverse()
    return ans


finp1 = open('inp1.txt', 'r')
inp1 = finp1.read()
finp2 = open('inp2.txt', 'r')
inp2 = finp2.read()
fout = open('output.txt', 'w')

fir = polyPairs(MyStrip(inp1))
sec = polyPairs(MyStrip(inp2))
answer = polySum(fir, sec)
print(f'Сумма полиномов равна (формат=[коэффициент, степень Х]: {answer}')
fout.write(str(answer))

finp1.close()
finp2.close()
fout.close()

# P.S. Да, я понимаю, что ОЧЕНЬ сильно переусложнил. И можно было сразу на входе получать полиномы в таком виде, к какому я его приводил посредством двух (!) функций. Но я пошёл на это сознательно.
