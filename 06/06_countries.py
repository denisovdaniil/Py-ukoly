# 06_countries.py

countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

print(countries)

countries_name = {}

for key, value in countries.items():
    countries_name[value]=key

print(countries_name)

countries_len = {}

for key, value in countries.items():
    countries_len[key]=len(value)

print(countries_len)
