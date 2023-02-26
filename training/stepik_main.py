'''
string = 'Hello my beautiful world!'

for i in range(len(string)):
    print(string[i])

for i in string:
    print(i)


count = 0
for i in string:
    if i == 'l':
        count += 1

#print(string.count('l'))



if 'my' in string:
    print(f'True, входит на позиции {string.find("my")}')
print(f'Букв l в строке {string.count("l")}')


n = input().lower()
count = 0

for i in range(len(n)):
    if n[i] == 'c' or n[i] == 'g':
        count += 1
print((count / len(n)) * 100)

n = input()

if n == n[::-1]:
    print('True')
else:
    print("False")


n = input().lower()
count = 1
i = 1

for i in range(len(n)):

    if n[i] == n[i + 1]:
        count += 1
    else:
        print(n[i] + str(count), end='')
        count = 1


students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)

x = [int(x) for x in input().split()]
print(sum(x))


x = [int(x) for x in input().split()]

for i in range(len(x)):
    if len(x) == 1:
        print(x[i])
        break
    elif i == 0:
        elem = x[i + 1] + x[-1]
        print(elem, end=' ')
    elif i == len(x) - 1:
        elem = x[len(x) - 2] + x[0]
        print(elem, end=' ')
    else:
        elem = x[i - 1] + x[i + 1]
        print(elem, end=' ')


x = [int(x) for x in input().split()]
minim = x[0]

for i in range(len(x)):
    if x[i] < minim:
        minim = x[i]
print(minim)
print(min(x))


summa = 0
sk = 0

while True:
    x = int(input())
    summa += x
    sk += x ** 2
    if summa == 0:
        break
print(sk)


x = int(input())
result = []

if x == 1:
    result.append(x)
elif x == 2:
    result.extend(x - 1, x)
else:
    for i in range(x):
        for j in range(i):
            if i <= x:
                result.append(i)
            else:
                break
print(*result[:x])

lst = [int(i) for i in input().split()]
x = int(input())

if x in lst:
    for i in range(len(lst)):
        if lst[i] == x:
            print(i, end=' ')
else:
    print('Отстуствует')


from random import randint

m, n = [int(i) for i in input().split()]

x = [[randint(1, 10) for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        print(x[i][j], end="\t")
    print()


x = []

while True:
    new_elem = input()
    if new_elem != 'end':
        x.append(new_elem.split())
    else:
        break

print(x)
________________________________________________

m, n = (int(i) for i in input().split())
x = []

# заполнение списка своими значениями

for i in range(m):
    row = input().split()
    for j in range(len(row)):
        row[j] = int(row[j])
    x.append(row)

# выполнение формулы

for i in range(m):
    for j in range(j):
        F = (x[i - 1], x[j]) + (x[i + 1], x[j]) + (x[i], x[j - 1]) + (x[i], x[j + 1])
        x[i][j] = F

# вывод списка
for i in range(m):
    for j in range(n):
        print(x[i][j], end=" ")
    print()
print(x)
___________________________________________________

total = 0
for i in range(11):
    num = int(input())
    if num != 0:
        total *= num
print(total)


for n in range(13):
    for k in range(12):
        for m in range(11):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f'n = {n} k = {k} m = {m}')


#10 * b + 5 * k + 0.5 * t == 100

for b in range(10):
    for k in range(20):
        for t in range(200):
            if 10 * b + 5 * k + 0.5 * t == 100 and b + k + t == 100:
                print(f'b = {b} k = {k} t = {t}')

#a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

for a in range(150):
    for b in range(150):
        for c in range(150):
            for d in range(150):
                for e in range(150):
                    if a != 0 and b != 0 and c != 0 and d != 0 and e != 0:
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            print(f'a = {a} b = {b} c = {c} d = {d} e = {e}')
                        #print(a + b + c + d + e)

n = int(input())

for i in range(1, n + 1):
    for m in range(1, i + 1):
        print(m, end='')
    for n in range(i - 1, 0, -1):
        print(n, end='')
    print()


for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3 and a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a ** 3 + b ** 3)

array = []
search = []
result = []
n = int(input())
counter = 0

for i in range(n):
    array.append(input())

k = int(input())

for j in range(k):
    search.append(input())

for i in range(len(array)):
    counter = 0
    for j in range(len(array)):
        if search[j].lower() in array[i].lower():
            counter += 1
    if counter == len(search):
        result.append(i)
print(result)

name = input('Введите название: ')
last_name = input('Введите расширение: ')

my_file = open(f'{name}.{last_name}', "w")
my_file.close()

import time
s = [int(i) for i in input().split()]

for i in range(len(s) - 1):
    for j in range(len(s) - i - 1):
        if s[j] > s[j + 1]:
            #print(f'{s[:j]}   ->{s[j:j + 2]}<-   {s[j + 2:]}')
            print(*s[:j], s[j:j + 2], *s[j + 2:], sep=' ')
            time.sleep(1)
            s[j], s[j + 1] = s[j + 1], s[j]

print(*s)

def get_factors(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(num)
    return result

n = int(input())

print(get_factors(n))

def get_next_prime(num):
    while is_prime(num) == False:
        num += 1
    else:
        return num


def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))


def is_palindrome(text):
    g = []
    for i in text:
        if i not in '.,!?- ':
            g.append(i)
    result = ''.join(g)
    return result.lower() == result[::-1].lower()


txt = input()

print(is_palindrome(txt))

# объявление функции

def is_chet(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False
def is_prime(num):
    counter = 0
    for i in range(1, int(num) + 1):
        if int(num) % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
def is_valid_password(num):
    if len(psw) <= 3:
        if psw[0] == psw[0][::-1] and is_prime(psw[1]) and is_chet(psw[2]):
            return True
        else:
            return False
    else:
        return False

# считываем данные
psw = input().split(':')

# вызываем функцию

print(is_valid_password(psw))

# объявление функции
def is_correct_bracket(text):
    b = 0
    for i in txt:
        if i == '(':
            b += 1
        if i == ')':
            b -+ 1
    if b == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


# объявление функции
def convert_to_python_case(text):
    result = txt
    for i in range(len(result)):
        if result[i].isupper() and i != 0:
            result[i] = f'_{result[i].lower()}'
    return result


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))


def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

def compute_binom(n, k):
    return int(fact(n) / (fact(k) * fact(n - k)))

n = int(input())
k = int(input())

print(compute_binom(n, k))

list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
list_2 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
          'семнадцать', 'восемнадцать', 'девятнадцать']
list_3 = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

def number_to_words(n):
    result = None
    if n < 10:
        result = list_1[n - 1]
    elif 10 < n < 20:
        result = list_2[n % 10 - 1]
    elif n % 10 == 0:
        result = list_3[n // 10 - 1]
    else:
        result = f'{list_3[n // 10 - 1]} {list_1[n % 10 - 1]}'
    return result

n = int(input())

print(number_to_words(n))

en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
      'december']

ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
      'декабрь']

def get_month(lang, num):
    if lang == 'en':
        return en[num]
    else:
        return ru[num]

language = input()
number = int(input())

print(get_month(language, number))


def is_magic(string):
    st = string.split('.')

    if int(st[0]) * int(st[1]) == int(st[2][-2:]):
        return True
    else:
        return False


string = input()

print(is_magic(string))


def is_pangram(s):
    s.lower()
    result = set(s.replace(' ', '').lower())

    if len(result) == 26:
        return True
    else:
        return False

string = input()

print(is_pangram(string))

from math import log2, ceil

n = int(input())
print(ceil(log2(n)))


#угадай-ка

from random import randint
from time import sleep

n = int((input('Угадайте число от 1 до 100: ')))
r_digit = randint(1, 100)
def is_valid(n):
    if 1 < n < 101:
        return n
    else:
        return False


while True:
    if is_valid(n):
        if n == r_digit:
            sleep(1)
            print('Вы победили!')
            break
        elif n > r_digit:
            n = int((input('Число больше загаданного: ')))
        elif n < r_digit:
            n = int((input('Число меньше загаданного: ')))


    else:
        n = int(input(('Введите корректные данные: ')))

is_valid(n)

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

def crypt(st, key):
    result = []
    for i in range(len(st)):
        if st[i] not in symbol:
            if st[i] in eng_upper_alphabet:
                st[i] = eng_upper_alphabet[i + key]
                result.append(st[i])
            #if st[i] in eng_lower_alphabet:
               # st[i] = eng_lower_alphabet[i + key]
               # result.append(st[i])
        else:
            result.append(st[i])
    return ''.join(result)

n = input('Введите строку для шифрования: ')
k = int(input('Введите ключ: '))

print(crypt(n, k))



/////////////////////////////////////////////////////////////////////////////////////////////

def caesar(alphabet):
    text = input('Введите строку для шифрования: ').split()
   #shift = int(input('Введите ключ: '))

    def get_char(char, alphabet_, shift_):
        if char.isalpha():
            i = 0
            if char.isupper():
                i = 1
            return alphabet_[i][(alphabet_[i].index(char) + shift_) % len(alphabet_[0])]
        return char

    #shifted = ''.join([get_char(char, alphabet, shift) for char in text])
    shifted = ''.join([get_char(char, alphabet, len(char)) for char in text])
    print(shifted)

def english_alphabet():
    return "".join([chr(char) for char in range(ord('a'), ord('z') + 1)])


caesar([english_alphabet(), english_alphabet().upper()])
/////////////////////////////////////////////////////////////////////////////////////////////


en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

n = input('Введите строку: ').split()

for i in n:
    counter = 0
    for j in i:
        if j.isalpha():
            counter += 1
    for j in i:
        if j.isupper():
            result += en_upper[(en_upper.find(j) + counter) % 26]
        elif j.islower():
            result += en_lower[(en_lower.find(j) + counter) % 26]
        else:
            result += j
    result += ' '
print(result)

#--------------------------------------------_----_--_-_---_-_-__-__------_----___-__-_--_-_-_
data_list = []

n = int(input())
while n != 'end':
    arr = []
    if n.isdigit():
        arr.append(n)
    else:
        data_list.append(arr)
    n = int(input())

print(data_list)



data_list = []

while True:
    row = input().split()
    if 'end' in row:
        break
    for i in range(len(row)):
        row[i] = int(row[i])
    data_list.append(row)

# логика заполнения
for i in range(len(data_list)):
    for j in range(len(data_list[i])):
        # result[i][j] = data_list[i - 1][j] + data_list[(i + 1) % m][j] + \
        #                  data_list[i][j - 1] + data_list[i][(j + 1) % m]
        print(data_list[i - 1][j] + data_list[i - len(data_list) + 1][j] + data_list[i][j - 1] +
              data_list[i][j - len(data_list[i]) + 1], end=" ")
    print()



n = int(input())
a = [[0] * n for i in range(n)]
count = 0

for i in range(n):
    count += 1
    a[0][i] = count

j = 0
i = n-1
n -= 1

while len(a)**2 != count:
    for _ in range(n):
        j += 1
        count += 1
        a[j][i] = count
    for _ in range(n):
        i -= 1
        count += 1
        a[j][i] = count
    for _ in range(n-1):
        j -= 1
        count += 1
        a[j][i] = count
    for _ in range(n-1):
        i += 1
        count += 1
        a[j][i] = count
    n -= 2

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()


def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return - x / 2
    else:
        return (x - 2) ** 2 + 1

x = float(input())

print(f(x))


def modify_list(l):
    for i in reversed(range(len(l))):
        if l[i] % 2 == 0:
            l[i] = l[i] // 2
        else:
            del l[i]
arr = [1, 3, 5, 7, 8]

print(modify_list(arr))


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif key not in d:
        if 2 * key in d:
            d[2 * key] += [value]
        else:
            d[2 * key] = [value]
    return d


d = {}
k = int(input())
v = int(input())

print(update_dictionary(d, k, v))


n = [i.lower() for i in input().split()]
d = {}

for i in n:
    d[i] = n.count(i)
for key, value in d.items():
    print(key, value)


def f(x):
    return x + 1

n = int(input())
arr = [int(input()) for i in range(n)]
d = {}

for i in arr:
    if i in d:
        print(d[i])
    else:
        d[i] = f(i)
        print(d[i])


with open('failik.txt', 'w') as data:
    n = input()
    while n != 'стоп':
        data.write(f'{n}\n')
        n = input()


with open('/Users/yarik/Downloads/dataset_3363_2-2.txt', 'r') as st:
    data = st.readline()

nums = []
num = ''
symb = []

for i in range(len(data)):
    if data[i].isdigit():
        num += data[i]
    else:
        if num != '':
            nums.append(int(num))
            num = ''
if num != '':
    nums.append(int(num))

for i in data:
    if i.isalpha():
        symb.append(i)



with open('/Users/yarik/Desktop/result.txt', 'w') as res:
    for i in range(len(symb)):
        res.write(symb[i] * nums[i])


with open('/Users/yarik/Downloads/dataset_3363_3-4.txt', 'r') as st:
    n = st.read().strip().split()
print(n)
d = {}

for i in n:
    d[i] = n.count(i)

mx = -1
res = ''
for value in d.values():
    if value > mx:
        mx = value

for k, v in d.items():
    if v == mx:
        res = k, v

print(*res)


with open('/Users/yarik/Downloads/dataset_3363_4-3.txt', 'r') as st:
    data = []
    for i in st:
        row = i.strip().split(';')
        data.append(row)

ln = len(data)

middle_1 = 0
middle_2 = 0
middle_3 = 0
for i in data:
    middle_1 += int(i[1])
    middle_2 += int(i[2])
    middle_3 += int(i[3])

with open('/Users/yarik/Desktop/result.txt', 'w') as st:
    for i in data:
        st.write(f'{(int(i[1]) + int(i[2]) + int(i[3])) / 3}\n')
    st.write(f'{middle_1 / ln} {middle_2 / ln} {middle_3 / ln}')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#with open('/Users/yarik/Desktop/data.txt', 'w') as st:
#    n = input()
#    while n != 'stop':
#        st.write(f'{n}\n')
#        n = input()

from time import ctime, sleep, time
import socket

with open('/Users/yarik/Desktop/data.txt', 'r') as st:
    data = []
    for i in st:
        data.append(i.strip())

result = []
import http.client
conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
print(conn.getresponse().read())

print('started')

with open('/Users/yarik/Desktop/logs.txt', 'a') as logs:
    logs.write(f'***start {ctime()}\n')

    for i in range(len(data)):
        if int(data[i]) > 10:
            result.append('up_ten')
            logs.write(f'dig upgrade <up_ten> {time()}\n')
        else:
            result.append('down_ten')
            logs.write(f'dig upgrade <down_ten> {time()}\n')
        sleep(0.3)

    logs.write(f'---finish {ctime()}\n')

with open('/Users/yarik/Desktop/res.txt', 'w') as res:
    for i in range(len(result)):
        res.write(f'{i + 1}) {result[i]}\n')

print('process finished')
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import requests

with open('/Users/yarik/Downloads/dataset_3378_3.txt', 'r') as st:
    data = st.readline().strip()

n = requests.get(f'{data}')

while not n.text.startswith('We'):
    data = n.text
    n = requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{data}')
    print(data)

result = requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{data}')
print(result.text)
///////////////////////////////////////////////////////
n = int(input())
arr = []
d = {}

for _ in range(n):
    arr.append(input().strip().split(';'))

for i in arr:
    if i[0] not in d.keys():
        d.setdefault(i[0], [0, 0, 0, 0, 0])
    if i[2] not in d.keys():
        d.setdefault(i[2], [0, 0, 0, 0, 0])

for i in arr:
    d[i[0]][0] += 1
    d[i[2]][0] += 1
    if int(i[1]) > int(i[3]):
        d[i[0]][1] += 1
        d[i[2]][3] += 1
        d[i[0]][4] += 3
    elif int(i[1]) < int(i[3]):
        d[i[0]][3] += 1
        d[i[2]][1] += 1
        d[i[2]][4] += 3
    else:
        d[i[0]][2] += 1
        d[i[2]][2] += 1
        d[i[0]][4] += 1
        d[i[2]][4] += 1

for key, value in d.items():
    print(f'{key}:', end='')
    print(*value)
///////////////////////////////////////////////////////

a = input()
b = input()
crypt = input()
decrypt = input()

for i in crypt:
    print(b[a.find(i)], end='')
print()
for i in decrypt:
    print(a[b.find(i)], end='')

n = int(input())
data = []

for _ in range(n):
    data.append(input().lower())

n = int(input())
st = []

for _ in range(n):
    st.append(input().lower().split())

result = set()
for i in st:
    for j in i:
        if j not in data:
            result.add(j)
for i in result:
    print(i)

data = []
x, y = 0, 0

for _ in range(int(input())):
    data.append(input().split())

for i in data:
    if i[0] == 'север':
        y += int(i[1])
    elif i[0] == 'запад':
        x -= int(i[1])
    elif i[0] == 'юг':
        y -= int(i[1])
    else:
        x += int(i[1])

print(x, y)



with open('/Users/yarik/Downloads/dataset_3380_5-2.txt', 'r') as f:
    p = []
    d = {}
    for l in f:
        p.append(l.strip('\n').split('\t'))
    print(p)
    for y in p:
        y[0] = int(y[0])
        y[2] = int(y[2])
    print(p)
    for c in p:
        if int(c[0]) in d:
            d[c[0]].append(c[2])
        else:
            d[c[0]] = [c[2]]

for k in sorted(d.keys()):
    x = (float(sum(d[k]) / len(d[k])))
    print(str(k) + ' ' + str(x))

    теперь я начал курс по основам и применению питона


n = int(input())
total = 0
for _ in range(n):
    total += int(input())
print(total)


a = 34
print(id(a))
a = 33
print(id(a))


objects = [1, 2, 1, 5, 1, 2]

g = []
for i in objects:
    if i not in g:
        g.append(i)
print(len(g))
print(len(set( objects)))


def decorator(func):

    def inner(n, counter=0):
        print('start')
        func(n, counter=0)
        for i in n:
            if i[0].lower() == i[-1].lower():
                counter += 1
        print(counter)
        print('finish')

    return inner

n = ['asd', 'asa', 'dad', 'xcv', 'e.']
@decorator
def inp(n):
    #n = [i.strip() for i in input().split(',')]
    n[-1] = n[-1][:-1]
    return n

print(decorator(inp(n)))

def decorator(func):
    def wrapper(*args, **kwargs):
        words = func(*args, **kwargs)
        count = 0
        for word in words:
            if word[0] == word[-1]:
                count += 1
        return count
    return wrapper

@decorator
def inp():
    n = [i.strip() for i in input().split(',')]
    n[-1] = n[-1][:-1]
    return n

print(inp())

def closest_mod_5(x):
    for y in range(x, x ** 2):
        if y % 5 == 0:
            return y

def ss(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(ss(3, 2, 5, 7, 1, 45, 7))



def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


print(s(21))
print(s(5, 5, 5, 5, 1))
print(s(0, 0, 31))
print(s(11, 10))
#print(s(b=31, 0))
print(s(11, b=20))
print(s(11, 10, 10))
#print(s(b=31))
print(s(11, 10, b=10))

n, k = [int(i) for i in input().split()]
def f(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return f(n - 1, k) + f(n - 1, k - 1)

print(f(n, k))


def add(ns, arg):
    scopes[ns]['variables'].add(arg)
def get(ns, arg):
    global result
    if arg in scopes[ns]['variables']:
        result.append(ns)
    elif scopes[ns]['parent'] is None and arg not in scopes[ns]['variables']:
        result.append(None)
    else:
        ns = scopes[ns]['parent']
        get(ns, arg)
def create(ns, parent):
    scopes[ns] = {'parent': parent, 'variables': set()}

n = int(input())
scopes = {'global': {'parent': None, 'variables': set()}}
result = []

for _ in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'add':
        add(namespace, arg)
    elif cmd == 'get':
        get(namespace, arg)
    else:
        create(namespace, arg)

for i in result:
    print(i)

class MyClass:
    def __init__(self, start=5):
        self.count = start
    def up(self, start=1):
        self.count += start
    def reset(self, start=0):
        self.count = start

x = MyClass()
print(x.count)
x.up()
print(x.count)
x.up(2)
print(x.count)
x.reset()
print(x.count)
x.reset(1)
print(x.count)

class MoneyBox:
    def __init__(self, capacity):
        self.data = 0
        self.max = capacity

    def can_add(self, v):
        if self.data + v <= self.max:
            return True
        else:
            return False
    def add(self, v):
        if self.can_add(v):
            self.data += v

class Buffer:
    def __init__(self):
        self.data = []
    def add(self, *a):
        self.data += a
        while len(self.data) >= 5:
            print(sum(self.data[:5]))
            self.data = self.data[5:]

    def get_current_part(self):
        print(self.data)

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()

n = int(input())
d_data, d_call = {}, []

for _ in range(n):
    row = input().split(':')
    d_data[row[0].strip()] = row[-1].strip().split()
n = int(input())
for _ in range(n):
    row = input().strip().split()
    d_call.append(row)

d_data = {
    'G': ['F'],
    'A': ['A'],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C'],
    'E': ['D'],
    'F': ['D'],
    'X': ['X'],
    'Y': ['X', 'A'],
    'Z': ['X'],
    'V': ['Z', 'Y'],
    'W': ['V'],
}
d_call = [
    'A G',      # Yes   # A предок G через B/C, D, F
    'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    'X W',      # Yes   # X предок W через Y, V
    'X QWE',    # No    # нет такого класса QWE
    'A X',      # No    # классы есть, но они нет родства :)
    'X X',      # Yes   # родитель он же потомок
    '1 1',      # No    # несуществующий класс
]


def find_path(graph, end, start, path=[]):
    path = path + [start]

    if start not in graph:
        return False
    if start == end:
        return True

    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, end, node, path)
            if newpath:
                return newpath
    return False

for i in d_call:
    if find_path(d_data, i[0], i[-1]):
        print('Yes')
    else:
        print('No')

class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())
    def sub(self):
        self.append(self.pop() - self.pop())
    def mul(self):
        self.append(self.pop() * self.pop())
    def div(self):
        self.append(self.pop() // self.pop())

ex = ExtendedStack([1, 2, 4, 5, 6, 7, 8, 3])
ex.sum()
ex.sub()
ex.mul()
ex.div()

class LoggableList(list, Loggable):
    def append(self, elem):
        super(LoggableList, self).append(elem)
        self.log(elem)

a = []
b = {}
c = ()
class My(list):
    name = 'Grigory'
    lastname = 'Vans'

print(My.__dict__)
delattr(My, 'name')
print(My.__dict__)
setattr(My, 'x', 43)
print(My.__dict__)

try:
    def f(a):
        if a > 0:
            return True
except False:
    print('тип поменяй придурок')

f(-1)
print('end')


data = {}
ex = []

for _ in range(int(input())):
    row = input().split(':')
    data[row[0].strip()] = row[-1].strip().split()

req = [input().strip() for i in range(int(input()))]

def func(age):
    if 18 < age <= 64:
        print('Door is opened...')
    else:
        raise ValueError('Please try again...')

func(int(input()))

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError('ne positiv')
        else:
            print(super(PositiveList, self).append(x)

class NonPositiveError(Exception):
    pass

x = PositiveList()
x.append(9)


import datetime

g = input().split()
d = int(input())
data = [int(i) for i in g]

cur_time = datetime.date(data[0], data[1], data[2])
delta =  datetime.timedelta(days=d)
print((cur_time + delta).strftime('%Y %-m %-d'))

import simplecrypt
with open('/Users/yarik/Downloads/passwords.txt', 'r') as file:
    data = [i.strip() for i in file.readlines()]

with open('/Users/yarik/Downloads/encrypted.bin', 'rb') as file:
    encrypt = file.read()
    for password in data:
        try:
            res = simplecrypt.decrypt(password, encrypt)
            print(f"{res.decode('utf8')} >>> {password}")
        except simplecrypt.DecryptionException:
            print('lame®')

print(data)

n = int(input())
data, req = {}, []

for _ in range(n):
    row = input().split(':')
    data[row[0].strip()] = row[-1].strip().split()
n = int(input())
for _ in range(n):
    req.append(input().strip())

data = {
    'G': ['F'],
    'A': ['A'],
    'B': ['A'],
    'C': ['A'],
    'D': ['B', 'C'],
    'E': ['D'],
    'F': ['D'],
    'X': ['X'],
    'Y': ['X', 'A'],
    'Z': ['X'],
    'V': ['Z', 'Y'],
    'W': ['V'],
}
req = [
    ['A', 'G'],      # Yes   # A предок G через B/C, D, F
    ['A', 'Z'],      # No    # Y потомок A, но не Y
    ['A', 'W'],      # Yes   # A предок W через Y, V
    ['X', 'W'],      # Yes   # X предок W через Y, V
    ['X', 'QWE'],    # No    # нет такого класса QWE
    ['A', 'eX'],      # No    # классы есть, но они нет родства :)

]

n = int(input())
data, req = {}, []

for _ in range(n):
    row = input().split(':')
    data[row[0].strip()] = row[-1].strip().split()
n = int(input())
for _ in range(n):
    req.append(input().strip())

result = []
def func(graph, elem, exc, path=[]):
    path = path + [elem]

    if elem not in graph:
        return None


    for node in graph[elem]:
        if node == elem:
            break
        if node in exc:
            if node not in result:
                return elem
            else:
                break

        elif node not in exc and node not in path:
            func(graph, node, exc, path)


exc = []
for i in req:
    exc.append(i)
    print(func(data, i, exc))

from random import randint
class RanIter:
    def __iter__(self):
        return self
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return randint(1, 10)
        else:
            raise StopIteration


for i in RanIter(10):
    print(i)

class DIB:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 3
            return self.lst[self.i - 3], self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        return DIB(self)

arr = [1, 4, 3, 6, 2, 3, 9, 2, 4]
for i in MyList(arr):
    print(i)

def f():
    print('chp 1')
    yield 1
    print('chp2')
    yield 2
    print('chp3')
    yield 3
    return 'End'

g = f()
print(next(g))
print(next(g))
print(next(g))

import itertools
def is_prime(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False

def primes():
    a = 2
    while True:
        if is_prime(a):
            yield a
        a += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))

from random import randint
class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False
    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False
    def judge_all(pos, neg):
        if neg == 0:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
    def __iter__(self):
        for i in self.iterable:
            self.pos, self.neg = 0, 0
            for j in self.funcs:
                if j(i) is True:
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self.pos, self.neg):
                yield i

def f1(x):
    return x % 5 == 0
def f2(x):
    return x % 2 == 0
def f3(x):
    return x % 3 == 0

n = int(input('input your len array: '))
arr = [randint(1, 50) for i in range(n)]



print(list(multifilter(arr, f1, f2, f3, judge=multifilter.judge_half)))
print(list(multifilter(arr, f1, f2, f3, judge=multifilter.judge_all)))
print(list(multifilter(arr, f1, f2, f3, judge=multifilter.judge_any)))

with open('/Users/yarik/Downloads/dataset_24465_4.txt', 'r') as f, open('result.txt', 'w') as w:
    for i in reversed(list(f)):
        w.write(i)

import os
result = []

for cur_dir, dirs, files in os.walk('main'):
    for file in files:
        if file.endswith('.py'):
            result.append(f'{cur_dir}')
            break
with open('result.txt', 'w') as f:
    for i in sorted(result):
        f.write(i + '\n')

def mod_checker(x, mod=0):
    return lambda y : y % x == mod

mod_5 = mod_checker(5)
print(mod_5(10))

s, a, b = input(), input(), input()
counter = 0

def func(s, a, b, counter):
    if a in s and a in b or counter >= 1000:
        return 'Impossible'
    elif a not in s:
        return 0
    else:
        counter += 1
        s = s.replace(a, b)
        if a in s:
            print(counter)
            func(s, a, b, counter)
        else:
            return counter


print(func(s, a, b, counter))

s, a, b = input(), input(), input()
counter = 0

while counter <= 1000:
    if a in s and a in b:
        print('Impossible')
        break
    elif a not in s:
        print(0)
        break
    else:
        counter += 1
        s = s.replace(a, b)
        if a not in s:
            print(counter)
            break

s, t, count = input(), input(), 0

while t in s:
    if s.startswith(t):
        count += 1
    s = s[1:]

print(count)

import asyncio
async def func1():
    print(1)

async def func2():
    await asyncio.sleep(10)
    print(2)

async def func3():
    print(3)

async def main():

    a = asyncio.create_task(func1())
    b = asyncio.create_task(func2())
    c = asyncio.create_task(func3())

    await asyncio.gather(a, b, c)

asyncio.run(main())

import re
import sys

pattern = r'\b([aA]+)\b'

for line in sys.stdin:
    line = line.rstrip()
    # if re.search(pattern, line):
    #     print(line)

    print(re.sub(pattern, 'argh', line, 1, re.IGNORECASE))


import re
import sys

pattern = r'\A[01]+\Z'

for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line) and int(line, 2) % 3 == 0:
        print(line)


print(int('10010', 2))

import requests
from bs4 import BeautifulSoup

a, b = input(), input()
response = requests.get(a)
soup = BeautifulSoup(response.text, 'lxml')

urls = soup.find_all('a')

for url in urls:
    print(url.text)

    print(b)
'''
a, b = input(), input()
if abs(int(a.split('/')[-1][6]) - int(b.split('/')[-1][6])) == 2:
    print('Yes')
else:
    print('No')


