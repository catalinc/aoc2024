import sys


def parse_map(map_str):
    return [list(map(to_height, line)) for line in map_str.strip().split("\n")]


def to_height(s, default=100):
    try:
        return int(s)
    except ValueError:
        return default


def find_trailheads(topographic_map):
    trailheads = []
    for y, row in enumerate(topographic_map):
        for x, height in enumerate(row):
            if height == 0:
                trailheads.append((y, x))
    return trailheads


def is_valid_move(topographic_map, y, x, current_height):
    rows, cols = len(topographic_map), len(topographic_map[0])
    return (
        0 <= y < rows and 0 <= x < cols and topographic_map[y][x] == current_height + 1
    )


def find_reachable_nines(topographic_map, start_y, start_x):
    visited = set()
    stack = [(start_y, start_x, 0)]
    reachable_nines = set()

    while stack:
        y, x, height = stack.pop()
        if (y, x) in visited:
            continue
        visited.add((y, x))

        if height == 9:
            reachable_nines.add((y, x))
            continue

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if is_valid_move(topographic_map, ny, nx, height):
                stack.append((ny, nx, height + 1))

    return reachable_nines


def calculate_trailhead_scores(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_score = 0

    for y, x in trailheads:
        reachable_nines = find_reachable_nines(topographic_map, y, x)
        total_score += len(reachable_nines)

    return total_score


def part1(topographic_map):
    return calculate_trailhead_scores(topographic_map)


def find_distinct_trails(topographic_map, start_y, start_x):
    visited = set()
    stack = [(start_y, start_x, 0, [])]
    distinct_trails = set()

    while stack:
        y, x, height, path = stack.pop()
        h = hash(f"{y},{x},{height},{path}")
        if h in visited:
            continue
        visited.add(h)

        new_path = path + [(y, x)]
        if height == 9:
            distinct_trails.add(tuple(new_path))
            continue

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if is_valid_move(topographic_map, ny, nx, height):
                stack.append((ny, nx, height + 1, new_path))

    return distinct_trails


def calculate_trailhead_ratings(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_rating = 0

    for y, x in trailheads:
        distinct_trails = find_distinct_trails(topographic_map, y, x)
        total_rating += len(distinct_trails)

    return total_rating


def part2(topographic_map):
    return calculate_trailhead_ratings(topographic_map)


def main():
    input_file = "input/day10.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    with open(input_file) as file:
        topographic_map = parse_map(file.read())
    print(part1(topographic_map))
    print(part2(topographic_map))


if __name__ == "__main__":
    main()
