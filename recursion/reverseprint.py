def reverse_print(value):
    if value < 0:
        raise ValueError("Value cannot be negative")
    if value == 1:
        print(value)
        return value
    else:
        print(value)
        reverse_print(value - 1)


reverse_print(10)
reverse_print(-3)

