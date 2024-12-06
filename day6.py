import sys


def parse_map(file_path):
    with open(file_path, "r") as file:
        map_data = []
        for line in file:
            map_data.append(list(line.strip()))
    return map_data


def find_guard_position(map_data, target="^"):
    for row_index, row in enumerate(map_data):
        for col_index, cell in enumerate(row):
            if cell == target:
                return (row_index, col_index)
    return None


N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)

ROT = {N: E, E: S, S: W, W: N}


def simulate_guard_patrol(map_data, initial_position, initial_direction=N):
    path = set()
    current_position = initial_position
    current_direction = initial_direction
    is_loop = False

    while True:
        path.add((current_position, current_direction))
        next_position = (
            current_position[0] + current_direction[0],
            current_position[1] + current_direction[1],
        )

        if (
            next_position[0] < 0
            or next_position[0] >= len(map_data)
            or next_position[1] < 0
            or next_position[1] >= len(map_data[0])
        ):
            break

        if map_data[next_position[0]][next_position[1]] == "#":
            current_direction = ROT[current_direction]
        else:
            current_position = next_position
        if (current_position, current_direction) in path:
            is_loop = True
            break

    return path, is_loop


def part1(map_data):
    guard_position = find_guard_position(map_data)
    path, _ = simulate_guard_patrol(map_data, guard_position)
    return len(set(p[0] for p in path))


def part2(map_data):
    guard_position = find_guard_position(map_data)
    path, _ = simulate_guard_patrol(map_data, guard_position)
    loop_positions = []
    unique_positions = set(p[0] for p in path)
    for position in unique_positions:
        if position != guard_position:
            original_value = map_data[position[0]][position[1]]
            map_data[position[0]][position[1]] = "#"
            _, is_loop = simulate_guard_patrol(map_data, guard_position)
            if is_loop:
                loop_positions.append(position)
            map_data[position[0]][position[1]] = original_value
    return len(set(loop_positions))


def main():
    input_file = "input/day6.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    map_data = parse_map(input_file)
    print(part1(map_data))
    print(part2(map_data))


if __name__ == "__main__":
    main()
