# coding=utf-8

def enhance(func):
    def new_func(*args):
        if len(args) == 0:
            return 0
        for v in args:
            if not isinstance(v, int):
                return 0
        return func(*args)
    return new_func

@enhance
def my_sum(*args):
    return sum(args)


@enhance
def my_avg(*args):
    return sum(args) / len(args)

print my_sum(1,2,3,4,5)
print my_sum(1,2,3,4,5, '6')
print my_avg(1,2,3,4,5)
print my_avg()