
my_dict = {'a': 1, 'b': 2, 'c': 3}


def fun1(*args):

    for arg in args:
        print(arg)


fun1(*my_dict)


def fun2(**kwargs):
 for key, value in kwargs.items():
        print(f"{key}: {value}")


fun2(**my_dict)

fun2(my_dict)