
# *args는 파라미터를 몇개를 받을지 모르는 경우 사용한다. args 는 튜플 형태로 전달된다.
#
def print_param(*args):
    print(args)
    for p in args:
        print(p)

print_param('a', 'b', 'c', 'd')

def print_param2(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

    for name, value in kwargs.items():
        print("%s : %s" % (name, value))

print_param2(first = 'a', second = 'b', third = 'c', fourth = 'd')