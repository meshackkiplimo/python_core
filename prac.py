def to_celsius(f):
    c=  (f - 32) * 5/9
    return c

def test(f):
    c = (to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)
