from code.code_math import add, sub

def add():
    assert add(2, 3) == 5
    assert add(2, 4) == 5
    assert add(2, 1) == 3

def sub():
    assert sub(2,3) ==1
    assert sub(2,23) ==13
    assert sub(2,342) ==3