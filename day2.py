import sys


def read_reports(file_path):
    reports = []
    with open(file_path, "r") as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            reports.append(report)
    return reports


def is_safe(report):
    increasing = all(x < y for x, y in zip(report, report[1:]))
    decreasing = all(x > y for x, y in zip(report, report[1:]))
    small_variation = all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))
    return (increasing or decreasing) and small_variation

def part1(reports):
    return sum(is_safe(report) for report in reports)

def is_safe_with_problem_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def part2(reports):
    return sum(is_safe_with_problem_dampener(report) for report in reports)

def main():
    input_file = "input/day2.txt"
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    reports = read_reports(input_file)
    print(part1(reports))
    print(part2(reports))

if __name__ == "__main__":
    main()