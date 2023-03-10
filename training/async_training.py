'''def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('yarik')
g2 = gen2(5)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
_______________________________

import socket
from select import select

tasks = []

to_read = {}
to_write = {}
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'hello world\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response)

        client_socket.close()

def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:

            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')

tasks.append(server())
event_loop()
'''

# def coroutine(func):
#     def inner(*args, **kwargs):
#         g = func(*args, **kwargs)
#         g.send(None)
#         return g
#     return inner

# @coroutine
# def average():
#     count, total, average = 0, 0, None
#
#     while True:
#         try:
#             x = yield average
#         except StopIteration:
#             print('Done!')
#             break
#         else:
#             count += 1
#             total += x
#             average = round(total / count, 2)
#
#     return average

# def subgen():
#     while True:
#         try:
#             message = yield
#         except    StopIteration:
#             print('exStopIt')
#             break
#         else:
#             print('...', message)
#     return 'returned from subgen()'
#
# @coroutine
# def delegator(g):
#     result = yield from g
#     print(result)

import asyncio
# import aiohttp

async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)

async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds passed')
        count += 1
        await asyncio.sleep(1)
async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    asyncio.run(main())

