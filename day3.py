import re
import sys


def parse_mul_instructions(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, content)

    return matches


def part1(mul_instructions):
    total = 0
    for instruction in mul_instructions:
        numbers = re.findall(r"\d{1,3}", instruction)
        numbers = list(map(int, numbers))
        result = numbers[0] * numbers[1]
        total += result
    return total


def parse_all_instructions(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, content)

    return matches


def part2(instructions):
    total = 0
    enabled = True
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        else:
            if enabled:
                numbers = re.findall(r"\d{1,3}", instruction)
                numbers = list(map(int, numbers))
                result = numbers[0] * numbers[1]
                total += result
    return total


def main():
    input_file = "input/day3.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    print(part1(parse_mul_instructions(input_file)))
    print(part2(parse_all_instructions(input_file)))


if __name__ == "__main__":
    main()
