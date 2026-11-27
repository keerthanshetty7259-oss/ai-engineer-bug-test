def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    total = 0.0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)
