from itertools import product
import sys


def parse_input(file_path):
    equations = []
    with open(file_path, "r") as file:
        for line in file:
            test_value, numbers = line.strip().split(":")
            numbers = list(map(int, numbers.split()))
            equations.append((int(test_value), numbers))
    return equations


def can_solve_equation(test_value, numbers):
    operators = ["*", "+", "||"]
    for ops in product(operators, repeat=len(numbers) - 1):
        expression = [numbers[0]]
        for num, op in zip(numbers[1:], ops):
            expression.append(op)
            expression.append(num)
        if evaluate_expression(expression) == test_value:
            return True
    return False


def evaluate_expression(expression):
    result = expression[0]
    i = 1
    while i < len(expression):
        operator = expression[i]
        next_number = int(expression[i + 1])
        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number
        elif operator == "||":
            result = int(f"{result}{next_number}")
        i += 2
    return result


def part1(data):
    total = 0
    for test_value, numbers in data:
        if can_solve_equation(test_value, numbers):
            total += test_value
    return total


def main():
    input_file = "input/day7.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    data = parse_input(input_file)
    print(part1(data))


if __name__ == "__main__":
    main()
