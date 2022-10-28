def is_dict(dictionary):
    if not isinstance(dictionary, dict):
        return False
    return True


def is_set(dictionary):
    if not isinstance(dictionary, set):
        return False
    return True


def check_input_dict_validator(validation_rules, dictionary):
    if not is_set(validation_rules) or not is_dict(dictionary):
        return False

    for rule in validation_rules:
        if len(rule) != 4:
            return False
    return True


def validate_dict(validation_rules, dictionary):
    if not check_input_dict_validator(validation_rules, dictionary):
        return "Invalid input"

    for rule in validation_rules:
        value = dictionary.get(rule[0])

        if value is None:
            return False

        if not value.startswith(rule[1]) or not value.__contains__(
                rule[2]) or not value.endswith(rule[3]):
            return False
    return True


def exercise5(validation_rules, dictionary):
    return validate_dict(validation_rules, dictionary)


dict1 = {"book": "Time-Block Planner", "author": "Cal Newport", "year": 2020}
dict2 = {"book": "Time-Block Planner", "author": "Cal Newport", "year": 2120}

if __name__ == '__main__':
    print("ex5: ", exercise5({("book", "Time", "lock", "er"), ("author", "C", "w", "port")}, dict1))
