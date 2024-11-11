from typing import Iterator

def read()->Iterator[int]:
    for i in range(10):
        yield i

gen = read()

for i in gen:
    print(i)


def squares(numbers):
    print("input of squares",numbers)
    for number in numbers:
        yield number ** 2

def even_filter(numbers):
    print("input of filter",numbers)
    for number in numbers:
        if number % 2 == 0:
            yield number

# 使用示例
nums = range(10)
even_squares = squares(even_filter(nums))
print(list(even_squares))  # 输出: [0, 4, 16, 36, 64]
