def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    relult = (len(string), string.upper(), string.lower())
    return relult

def is_contains(string: str, list_to_search: list):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)