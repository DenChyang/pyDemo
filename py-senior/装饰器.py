def after(func):
    print("start")
    def after_in(*args):
        print("after")
        func(*args)
        print("before")
    print("end---")
    return after_in

@after
def test1(a):
    print("test1 %s"%a)

test1(1)