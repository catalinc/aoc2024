from collections import defaultdict
import sys


def transform_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid = len(str_stone) // 2
            left = int(str_stone[:mid])
            right = int(str_stone[mid:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stone * 2024)
    return new_stones


def simulate_blinks(stones, blinks):
    for i in range(blinks):
        stones = transform_stones(stones)
    return stones


def part1(stones):
    final_stones = simulate_blinks(stones, 25)
    return len(final_stones)


def transform_one_stone(stone):
    if stone == 0:
        return [1]
    s_stone = str(stone)
    if len(s_stone) % 2 == 0:
        mid = len(s_stone) // 2
        left = int(s_stone[:mid])
        right = int(s_stone[mid:])
        return [int(left), int(right)]
    return [stone * 2024]


def simulate_blinks_faster(stones, blinks):
    counts = {k: 1 for k in stones}
    for _ in range(blinks):
        new_counts = defaultdict(int)
        for stone, num in counts.items():
            for new_stone in transform_one_stone(stone):
                new_counts[new_stone] += num
        counts = new_counts
    return sum(counts.values())


def part2(stones):
    return simulate_blinks_faster(stones, 75)


def main():
    input_file = "input/day11.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    with open(input_file, "r") as file:
        initial_stones = list(map(int, file.readline().strip().split()))
    print(part1(initial_stones))
    print(part2(initial_stones))


if __name__ == "__main__":
    main()
