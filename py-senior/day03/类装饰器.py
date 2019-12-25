class Test():
    def __init__(self):
        print("--init--")

    def __call__(self, *args, **kwargs):
        print("--test--")

t = Test()
t()
print("===========")
print("1"==1)