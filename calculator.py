def divide_numbers(a: float, b: float) -> float:
    # Bug 1: Missing zero-division check
    return a / b


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    total = 0.0
    # Bug 2: Off-by-one error (skips the first element at index 0)
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total / len(numbers)
