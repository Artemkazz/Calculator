print('Калькулятор простых математических выражений\n', "Доступные операнды: \n", '+ сложение \n', '- вычитание\n', '/ деление\n', '* умножение\n')
s = input('Введите математическое выражение: ')
operands = ['*', '/', '+', '-']
a = ''
n = []
for i in s:
    if i not in operands:
        a += i
    else:
        n.append(int(a))
        n.append(i)
        a = ''
n.append(int(a))
while len(n) != 1:
    if '*' in n:
        i = n.index('*')
        a = n[i-1] * n[i+1]
        n[i] = a
        del n[i-1:i+2:2]
        continue
    if '/' in n:
        i = n.index('/')
        a = n[i-1] / n[i+1]
        n[i] = a
        del n[i-1:i+2:2]
        continue
    if '+' or '-' in n:
        if n[1] == '+':
            i = 1
            a = n[i-1] + n[i+1]
            n[1] = a
            del n[i-1:i+2:2]
            continue
        elif n[1] == '-':
            i = 1
            a = n[i-1] - n[i+1]
            n[1] = a
            del n[i-1:i+2:2]
            continue
print(*n)
