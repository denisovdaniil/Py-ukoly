# 15_get_upper_chars.py

def get_upper_chars(text):
    
    return ''.join([char for char in text if char.isupper()])




def test_get_upper_chars():

    assert get_upper_chars("") == ""
    assert get_upper_chars("ahoj JSEM") == "JSEM"
    assert get_upper_chars("Ahoj jsem teď v Praze") == "AP"
    assert get_upper_chars("jsem teď") == ""
    


test_get_upper_chars()
