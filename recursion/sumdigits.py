def sum_digits(value):
    if value < 0:
        raise ValueError("Must not be a negative")
    if value < 10:
        return value


sum_digits(123)
