import sys
import os
import psutil


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

def find_cycle(stone):
    cycle = 0
    new_stones = [stone]
    while True:
        new_stones = transform_stones(new_stones)
        cycle += 1
        if stone in new_stones:
            return cycle

def simulate_blinks(stones, blinks):
    for i in range(blinks):
        stones = transform_stones(stones)
        print("Blink {}: {} stones".format(i + 1, len(stones)))
        process = psutil.Process(os.getpid())
        print("Memory used: {} MB".format(process.memory_info().rss / 1024 ** 2))
    return stones


def part1(stones):
    final_stones = simulate_blinks(stones, 25)
    return len(final_stones)


def part2(stones):
    for stone in stones:
        print(f"{stone} found after {find_cycle(stone)} cycles")
    final_stones = simulate_blinks(stones, 5)
    return len(final_stones)


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
