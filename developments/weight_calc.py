import time

def broke(height, k):
    if height < 155:
        return round((height - 95) * k, 1)
    elif 155 < height < 175:
        return round((height - 100) * k, 1)
    else:
        return round((height - 110) * k, 1)

def coefficient_calc(i):
    if i < 15:
        return 0.9
    elif 15 < i < 17:
        return 1
    else:
        return 1.1

if __name__ == '__main__':


    with open('data.txt', 'w') as data:
        n = input()
        while n != 'stop':
            data.write(f'{n}\n')
            n = input()


    data = {}
    with open('data.txt', 'r') as st:
        file = st.readlines()
        for i in file:
            row = i.strip().split(';')
            data[row[0].strip()] = row[1:]


    for k in data:
        data[k] = [int(i) for i in data[k]]
        data[k][-1] = coefficient_calc(data[k][-1])


    with open('result.txt', 'a') as file:
        file.write(f'{time.ctime()}\n')
        for elem in data:
            file.write(f'Идеальный вес для {elem} составляет: {broke(data[elem][0], data[elem][-1])}\n')
        file.write(f'------------------\n')

    print(data)
    print('mission complete')




