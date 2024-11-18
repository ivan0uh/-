calls = 0


def count_cals(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        result = func(*args, **kwargs)
        return result

    return wrapper


def string_info(input_string):
    global calls
    calls += 1
    return (len(input_string), input_string.upper(), input_string.lower())


def is_contains(string, list_to_search):
    global calls
    calls += 1
    string_lower = string.lower()
    for item in list_to_search:
        if item.lower() == string_lower:
            return True
    return False


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))  # Urban ~ urBAN
print(is_contains("cycle", ["recycling", "cyclic"]))  # No matches
print(calls)
