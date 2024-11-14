from NicholasCompiler import *
print('running tests')
def runtests():
    test_Integer_add()

def test_Integer_add():
    a = Integer(11)
    b = Integer(9)
    c = Integer(1)
    d = Integer(5)
    print(a)
    print(a+c)
    assert a+a == 22
    assert a+c == 12
    assert c+a == a+c
    assert c+c == 2
    assert b+c == 11
    assert d+d == 11
    assert c+d == 6

try:
    runtests()
    print('All tests passed!')

except AssertionError as e:
    print('Test failed!')
    raise e
