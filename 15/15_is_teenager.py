# 15_is_teenager.py

def is_teenager(age):
    if 13 < age < 19:
        return True
    else:
        return False


def test_is_teenager():
    
    assert is_teenager(10) == False
    assert is_teenager(15) == True
    assert is_teenager(25) == False
    

test_is_teenager()
