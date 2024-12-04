import sys


def read_grid_from_file(file_path):
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file]
    return grid


def count_xmas_occurrences(grid):
    word = "XMAS"

    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(grid)
                or ny >= len(grid[0])
                or grid[nx][ny] != word[i]
            ):
                return False
        return True

    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
    count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_from_position(x, y, dx, dy):
                    count += 1

    return count


def part1(grid):
    return count_xmas_occurrences(grid)


def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    offsets = [
        ((-1, -1), (1, 1)),
        ((-1, 1), (1, -1)),
    ]

    def is_mas_pattern(start, end):
        chars = [grid[start[0]][start[1]], grid[end[0]][end[1]]]
        return chars == ["M", "S"] or chars == ["S", "M"]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] != "A":
                continue

            found_mas = True
            for offset in offsets:
                (dx1, dy1), (dx2, dy2) = offset
                x1, y1 = r + dx1, c + dy1
                x2, y2 = r + dx2, c + dy2

                if not (
                    0 <= x1 < rows
                    and 0 <= y1 < cols
                    and 0 <= x2 < rows
                    and 0 <= y2 < cols
                ):
                    continue

                if not is_mas_pattern((x1, y1), (x2, y2)):
                    found_mas = False
                    break
            if found_mas:
                count += 1
    return count


def part2(grid):
    return count_xmas_patterns(grid)


def main():
    file_path = "input/day4.txt"
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    grid = read_grid_from_file(file_path)
    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()
