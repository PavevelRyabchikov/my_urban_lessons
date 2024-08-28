# Домашнее задание по теме "Пространство имён", module_3_1.py

def count_calls(string_info, is_contains):
    global calls
    calls += 1
    return(calls)

def string_info(string):
    global calls
    calls += 1
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    global calls
    calls += 1
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string in list_to_search:
        return True
    else:
        return False

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

    
    
