# 08_regex.py

import re

rx_number = re.compile(r'^\d{9}$')
rx_number_space = re.compile(r'^\d{3} \d{3} \d{3}$')
rx_number_code = re.compile(r'^\+420\d{9}$')
rx_number_code_space = re.compile(r'^\+420 \d{3} \d{3} \d{3}$')

def check_phone_number(number):
    match_number = rx_number.search(number)
    match_number_space = rx_number_space.search(number)
    match_number_code = rx_number_code.search(number)
    match_number_code_space = rx_number_code_space.search(number)
    return any((
        match_number,
        match_number_space,
        match_number_code,
        match_number_code_space
        ))
    
print(check_phone_number('608229222'))
print(check_phone_number('608 229 222'))
print(check_phone_number('+420608229222'))
print(check_phone_number('+420 608 229 222'))

