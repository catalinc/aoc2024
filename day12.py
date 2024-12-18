def parse_map(map_str):
    return [list(line) for line in map_str.strip().split("\n")]


def find_regions(garden_map):
    rows, cols = len(garden_map), len(garden_map[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    def dfs(y, x, plant_type):
        stack = [(y, x)]
        region = []
        while stack:
            cy, cx = stack.pop()
            if visited[cy][cx]:
                continue
            visited[cy][cx] = True
            region.append((cy, cx))
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = cy + dy, cx + dx
                if (
                    0 <= ny < rows
                    and 0 <= nx < cols
                    and not visited[ny][nx]
                    and garden_map[ny][nx] == plant_type
                ):
                    stack.append((ny, nx))
        return region

    for y in range(rows):
        for x in range(cols):
            if not visited[y][x]:
                plant_type = garden_map[y][x]
                region = dfs(y, x, plant_type)
                regions.append((plant_type, region))

    return regions


def calculate_area_and_perimeter(region, garden_map):
    area = len(region)
    perimeter = 0
    rows, cols = len(garden_map), len(garden_map[0])

    for y, x in region:
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if (
                ny < 0
                or ny >= rows
                or nx < 0
                or nx >= cols
                or garden_map[ny][nx] != garden_map[y][x]
            ):
                perimeter += 1

    return area, perimeter


def calculate_total_price(garden_map):
    regions = find_regions(garden_map)
    total_price = 0

    for plant_type, region in regions:
        area, perimeter = calculate_area_and_perimeter(region, garden_map)
        price = area * perimeter
        total_price += price

    return total_price


def part1(garden_map):
    return calculate_total_price(garden_map)


def calculate_area_and_sides(region, garden_map):
    area = len(region)
    sides = 0
    rows, cols = len(garden_map), len(garden_map[0])
    visited = set(region)

    for y, x in region:
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if (ny, nx) not in visited:
                sides += 1

    return area, sides


def calculate_total_price_with_discount(garden_map):
    # FIXME: Not working
    regions = find_regions(garden_map)
    total_price = 0

    for plant_type, region in regions:
        area, sides = calculate_area_and_sides(region, garden_map)
        price = area * sides
        total_price += price

    return total_price


def part2(garden_map):
    return calculate_total_price_with_discount(garden_map)


def main():
    with open("input/day12.txt", "r") as file:
        input_map = file.read().strip()

    garden_map = parse_map(input_map)
    print(part1(garden_map))
    print(part2(garden_map))

if __name__ == "__main__":
    main()
