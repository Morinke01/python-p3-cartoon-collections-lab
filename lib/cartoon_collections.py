def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print (f"{index}. {dwarf}")


def summon_captain_planet(planeteer_calls):
    result = []
    for planet in planeteer_calls:
        result.append(f'{planet.capitalize()}!')
    return result

def long_planeteer_calls(call_list):
    for char in call_list:
        if len(char) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheese = ('cheddar','gouda','camembert')
    for string in strings:
        if string.lower() in cheese:
            return string
    return None
