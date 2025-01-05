# 07_countries.py

countries = {
    "Irsko": 4593100,
    "Chorvatsko": 4290612,
    "Moldavsko": 3559500,
    "Litva": 2941953,
    "Albánie": 2821977,
    "Slovensko": 5415949,
    "Norsko": 5109056,
    "Itálie": 59943933,
    "Španělsko": 46609700,
    "Ukrajina": 45426200,
    "Polsko": 38502396,
    "Mkedonie": 2062294,
    "Slovinsko": 2061963,
    "Lotyšsko": 2003900,
    "Kosovo": 1815606,
    "Estonsko": 1311870,
    "Rusko": 143700000,
    "Německo": 80619000,
    "Turecko": 76667864,
    "Francie": 65844000,
    "Velká Británie": 63705000,
    "Portugalsko": 10487289,
    "Maďarsko": 9906000,
    "Švédsko": 9651531,
    "Bělorusko": 9468100,
    "Rakousko": 8504850,
    "Švýcarsko": 8112200,
    "Bulharsko": 7282041,
    "Srbsko": 7181505,
    "Dánsko": 5627235,
    "Finsko": 5452821,
    "Rumunsko": 20121641,
    "Nizozemsko": 16842200,
    "Belgie": 11132269,
    "Řecko": 10815197,
    "Česko": 10513800,
}

number_countries = len(countries)

print(number_countries)

total_population = sum(countries.values())


print(total_population)

avg_population = total_population / number_countries

print('Average population is', round(avg_population))

def get_min(countries):
    min_key, min_value = next(iter(countries.items()))
    for key, value in countries.items():
        if value < min_value:
            min_key, min_value = key, value
    return min_key, min_value

key, value = get_min(countries)
print(f"The country with the lowest population is {key} with a population of {value}.")

def get_max(countries):
    max_key, max_value = next(iter(countries.items()))
    for key, value in countries.items():
        if value > max_value:
            max_key, max_value = key, value
    return max_key, max_value

key, value = get_max(countries)
print(f"The country with the highest population is {key} with a population of {value}.")

