from typing import Callable


def __passes_all_predicates(val: int, predicates: list[Callable[[int], bool]]) -> bool:
    for pred in predicates:
        if not pred(val):
            return False

    return True


def ex7(**kwargs) -> list[int]:
    HARD_LIMIT = 1000
    filters: list[Callable[[int], bool]] = []
    limit = 1000
    offset = 0

    if "filters" in kwargs:
        filters = kwargs["filters"]
        for filter in filters:
            if not isinstance(filter, Callable):
                raise ValueError("Filters must be predicates (int) -> bool")
    if "limit" in kwargs:
        try:
            limit = int(kwargs["limit"])
        except ValueError:
            raise ValueError("Limit parameter must be an int")
    if "offset" in kwargs:
        try:
            offset = kwargs["offset"]
        except ValueError:
            raise ValueError("Offset parameter must be an int")

    if limit > HARD_LIMIT:
        raise ValueError(
            f"Input value {limit} exceeds possible generated values {HARD_LIMIT}"
        )
    if offset > limit or offset > HARD_LIMIT or offset < 0:
        raise ValueError(f"Offset value should be 0 <= offset < {limit}")

    out: list[int] = []
    a = 0
    b = 1
    added = index = 0
    while added < limit:
        if not __passes_all_predicates(a, filters):
            a, b = b, a + b
            continue

        if index >= offset:
            out.append(a)
            added += 1

        a, b = b, a + b
        index += 1
    return out


if __name__ == '__main__':
    def sum_digits(x):
        return sum(map(int, str(x)))


    print(
        ex7(
            filters=[
                lambda item: item % 2 == 0,
                lambda item: item == 2 or 4 <= sum_digits(item) <= 20,
            ],
            limit=2,
            offset=2,
        )
    )
