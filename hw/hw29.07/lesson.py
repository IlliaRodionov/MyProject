from os import write
import sys

my_list = [i for i in range(50_000_000)]

my_iter = iter(my_list)

print(len(my_list))
print(sys.getsizeof(my_list))

for i in range(100):
    print(i)

ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
ii = iter(ll)
while True:
    try:
        print(next(ii))
    except StopIteration:
        break


def generator(n: int):
    i = 0
    while i < n:
        i += 1
        yield i


for i in generator(10):
    print(i)


def enhance(line: str):
    line.strip()
    return line


def writer(source: str, destination: str):
    write_file = open(destination, 'w+')

    with open(source) as source_file:
        while True:
            try:
                line = source_file.readline()
                write_file.write(enhance(line))
            except:
                break


def get_file_lines(filename: str):
    with open(filename) as source_file:
        while True:
            try:
                line = source_file.readline()
                yield line
            except:
                break


with open('write.txt', 'a') as write_file:
    for line in get_file_lines("read.txt"):
        write_file.write(enhance(line))

writer('source.txt', 'dst.txt')


def foo(n):
    for i in range(n):
        if i % 2 == 0:
            yield "Четное"
        else:
            yield i


for i in foo(10):
    print(i)
