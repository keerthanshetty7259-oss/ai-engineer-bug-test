def divide_numbers(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def calculate_average(numbers: list[float]) -> float:
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not numbers:
        return 0.0
    for i, n in enumerate(numbers):
        if not isinstance(n, (int, float)):
            raise ValueError(f"Element at index {i} must be a number")
    total = 0.0
    for n in numbers:
        total += n
    return total / len(numbers)
