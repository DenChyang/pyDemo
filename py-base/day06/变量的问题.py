#a = 100
a = [100]

def test(a):
    #a += a
    a = a + a
    print(a)

test(a)
print(a)