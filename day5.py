from collections import defaultdict
from collections import deque
import sys


def parse_input(filename: str):
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n")

    rules = defaultdict(set)
    queues = []
    is_queue_section = False

    for line in lines:
        if line == "":
            is_queue_section = True
            continue

        if is_queue_section:
            queue = list(map(int, line.split(",")))
            queues.append(queue)
        else:
            parent, child = map(int, line.split("|"))
            rules[parent].add(child)

    return rules, queues


def part1(rules, queues):
    all_valid = []
    for queue in queues:
        if is_valid_print_order(rules, queue):
            all_valid.append(queue)
    result = sum(queue[len(queue) // 2] for queue in all_valid)
    return result


def is_valid_print_order(rules, queue):
    for i in range(len(queue)-1):
        curr_page = queue[i]
        next_page = queue[i + 1]
        if next_page not in rules[curr_page]:
            return False
    return True


def part2(rules, queues):
    all_fixed = []
    for queue in queues:
        if not is_valid_print_order(rules, queue):
            fixed_queue = fix_print_order(rules, queue)
            all_fixed.append(fixed_queue)
    result = sum(queue[len(queue) // 2] for queue in all_fixed)
    return result


def fix_print_order(rules, queue):
    in_degree = {node: 0 for node in queue}
    for node in queue:
        for child in rules[node]:
            if child in in_degree:
                in_degree[child] += 1

    zero_in_degree_queue = deque([node for node in queue if in_degree[node] == 0])
    sorted_queue = []

    while zero_in_degree_queue:
        node = zero_in_degree_queue.popleft()
        sorted_queue.append(node)
        for child in rules[node]:
            if child in in_degree:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    zero_in_degree_queue.append(child)

    return sorted_queue

def main():
    input_file = "input/day5.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    rules, queues = parse_input(input_file)
    print(part1(rules, queues))
    print(part2(rules, queues))


if __name__ == "__main__":
    main()
