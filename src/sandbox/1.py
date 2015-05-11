__author__ = 'chrisshroba'

aa=dict()
def test(a,b,**c):
    global aa
    print a
    print b
    aa = c

test(1,2,al="a",bl="b",cl="c")
print aa