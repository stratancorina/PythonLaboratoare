import re


def get_days_from_month_regex(year: str, month: str) -> str:

    days_per_month = [
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|1\d|2[0-8])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])"
    ]
    try:
        if int(year) % 4 == 0:
            days_per_month[1] = r"(0[1-9]|1\d|2[0-9])"
        return days_per_month[int(month) - 1]
    except Exception as e:
        raise SystemError(e)


def get_control_digit(digits: str) -> str:
    checksum_number = "279146358279"
    checksum = 0
    for i, j in zip(checksum_number, digits):
        checksum += int(i) * int(j)
    checksum %= 11
    if checksum == 10:
        checksum = 1
    return str(checksum)


def ex_7(input_text: str) -> bool:
    match_first_digit = r"[1-8]"
    match_year = r"\d{2}"
    match_month = r"(0[1-9]|1[0-2])"
    match_day = get_days_from_month_regex(input_text[1:3], input_text[3:5])
    match_county = r"(0[1-9]|[1-3]\d|4[0-6]|5[1-2])"
    random_digits = r"(00[1-9]|0[1-9]\d|\d\d\d)"
    control_digit = get_control_digit(input_text[:-1])
    regex_string = r"^" + match_first_digit + match_year + match_month + match_day + match_county + random_digits + \
                   control_digit + r"$"
    print(regex_string)
    return bool(re.match(regex_string, input_text))

if __name__ == '__main__':
    print(ex_7("1730110155203"))
