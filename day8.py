from collections import defaultdict
import sys


def parse_input(file_path):
    with open(file_path, "r") as file:
        grid = [line.rstrip("\n") for line in file]
        rows = len(grid)
        cols = len(grid[0])
        antennas = {}
        for y in range(rows):
            for x in range(cols):
                char = grid[y][x]
                if char != ".":
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((y, x))
        return antennas, rows, cols


def find_antinodes(antennas, rows, cols):
    antinodes = set()

    def add_antinodes(y1, x1, y2, x2):
        dx, dy = x2 - x1, y2 - y1
        antinode1 = (x1 + 2 * dx, y1 + 2 * dy)
        antinode2 = (x2 - 2 * dx, y2 - 2 * dy)
        if 0 <= antinode1[0] < cols and 0 <= antinode1[1] < rows:
            antinodes.add(antinode1)
        if 0 <= antinode2[0] < cols and 0 <= antinode2[1] < rows:
            antinodes.add(antinode2)

    for positions in antennas.values():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                y1, x1 = positions[i]
                y2, x2 = positions[j]
                add_antinodes(y1, x1, y2, x2)

    return antinodes


def find_antinodes_updated(antennas, rows, cols):
    antinodes = set()

    def add_antinodes(y1, x1, y2, x2):
        step_x, step_y = x2 - x1, y2 - y1

        step = -1
        while True:
            x = x1 + step * step_x
            y = y1 + step * step_y
            if 0 <= x < cols and 0 <= y < rows:
                antinodes.add((y, x))
            else:
                break
            if x == 0 or x == cols - 1 or y == 0 or y == rows - 1:
                break
            step -= 1

        step = 1
        while True:
            x = x2 + step * step_x
            y = y2 + step * step_y
            if 0 <= x < cols and 0 <= y < rows:
                antinodes.add((y, x))
            else:
                break
            if x == 0 or x == cols - 1 or y == 0 or y == rows - 1:
                break
            step += 1

    for positions in antennas.values():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                y1, x1 = positions[i]
                y2, x2 = positions[j]
                add_antinodes(y1, x1, y2, x2)
                antinodes.add((y1, x1))
                antinodes.add((y2, x2))

    return antinodes


def part1(antennas, rows, cols):
    antinodes = find_antinodes(antennas, rows, cols)
    return len(antinodes)


def part2(antennas, rows, cols):
    antinodes = find_antinodes_updated(antennas, rows, cols)
    return len(antinodes)


def main():
    input_file = "input/day8.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    antennas, rows, cols = parse_input(input_file)
    print(part1(antennas, rows, cols))
    print(part2(antennas, rows, cols))


if __name__ == "__main__":
    main()
