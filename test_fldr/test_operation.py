import sys
import os

# Add the root folder to sys.path
sys.path.append(os.path.abspath("C:/Users/Public/Docker/CI-CD Pipelines"))

# Now you can import the code_math module
from code_fldr.code_math import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(2, 4) == 6
    assert add(2, 1) == 3

def test_sub():
    assert sub(3, 2) == 1
    assert sub(23, 13) == 10
    assert sub(342, 3) == 339

if __name__ == "__main__":
    test_add()
    test_sub()
    print("All tests passed!")
