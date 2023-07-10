123,124,125,126,999
for i in range(1,10):
    for q in range(2,10):
        for w in range(3,9):
            print(f'{i}{q}{w}',end = ',')
print(999)                
stroka = 'Петя'
print(stroka[1])

stroka = input('Введите слово ')
count = 0

for i in stroka:
    count += 1

print(count)

stroka = input('Введите слово ')

print(stroka * 3)

stroka = input('Введите слово ')

print(stroka[0])

stroka = input('Введите слово ')
print(stroka[0:3])

stroka = input('Введите слово ')
print(stroka[-3:])

stroka = input('Введите слово ')
print(stroka[::-1])

stroka = input('Введите слово ')
print(stroka[1:-1])

stroka = input('Введите слово ')
print(stroka[2])

stroka = input('Введите слово ')
print(stroka[-2])

stroka = input('Введите слово ')
print(stroka[0:5])

stroka = input('Введите слово ')
print(stroka[0:-2])

stroka = input('Введите слово ')
print(stroka[1::2])

stroka = input('Введите слово ')
print(stroka[::2])

stroka = input('Введите слово ')
print(stroka[::-2])

name = input()
fam = input()
print(f'{name[0]}.{fam[0]}')

for i in range(1,11,1):
    print(i)

i = 10

while i >= 1:
    print(i)
    i = i - 1

ot = int(input('Напишите число '))


while ot <= do :
    print(ot)
    ot += 1

ot = int(input())


while ot != 0 :
    print('Напишите число ')
    ot = int(input())

sum = int(input())
kol = 0

while sum != 0 :
    if sum - 15 >= 0:
        kol += 1
        sum -= 15
    elif sum - 10 >= 0:
        kol += 1
        sum -= 10
    elif sum - 5 >= 0:
        kol += 1
        sum -= 5
    elif sum - 1 >= 0 :
        kol += 1
        sum -= 1

print(kol)

sum = int(input())

while sum != 0 :
    print('*' * sum)
    sum -= 1
        
n = int(input())
a = 1
while a != 5:
    print('Ваше число ')
    n = int(input())

while True:
    print('Ваше число ')
    n = int(input())
    if n == 3:
        break
