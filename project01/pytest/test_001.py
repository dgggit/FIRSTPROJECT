import pytest

def test_001():
    print("jenkinks test")
def test_002():
    print("commit,push")

if __name__ == '__main__':
    pytest.main(['-s','test_001.py'])