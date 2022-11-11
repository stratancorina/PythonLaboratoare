def multiply_by_two(x):
    return x * 2


def multiply_by_three(x):
    return x * 3


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def new_function(*args, **kwargs):
        print(*args, **kwargs)
        return function(*args, **kwargs)

    return new_function


def multiply_output(function):
    def new_function(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return new_function


def argument_function(function, decorators):
    def new_function(*args, **kwargs):
        result = function
        for i in decorators:
            result = i(result)
        return result(*args, **kwargs)

    return new_function


if __name__ == "__main__":
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    print(augmented_multiply_by_two(3))
