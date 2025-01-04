# 04_file.py

hodnota = input('Zadejte hodnotu: ')

def append():
    
    with open('Py-ukoly/04/04_file.txt', mode = 'a', encoding = 'utf-8') as file:
        file.write(hodnota + "\n")

append()