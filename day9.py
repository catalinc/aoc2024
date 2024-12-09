import sys


def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    is_free_space = False
    for c in disk_map:
        if is_free_space:
            blocks.extend(["."] * int(c))
            is_free_space = False
        else:
            blocks.extend([file_id] * int(c))
            is_free_space = True
            file_id += 1
    return blocks


def compact_disk(blocks):
    n = len(blocks)
    for i in range(n - 1, -1, -1):
        if blocks[i] != ".":
            for j in range(i):
                if blocks[j] == ".":
                    blocks[j] = blocks[i]
                    blocks[i] = "."
                    break
    return blocks


def calculate_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        if block != ".":
            checksum += i * block
    return checksum


def part1(blocks):
    compacted_blocks = compact_disk(blocks)
    checksum = calculate_checksum(compacted_blocks)
    return checksum


def compact_disk_whole_files(blocks):
    n = len(blocks)
    file_positions = {}

    for i in range(n):
        if blocks[i] != ".":
            file_id = blocks[i]
            if file_id not in file_positions:
                file_positions[file_id] = []
            file_positions[file_id].append(i)

    for file_id in sorted(file_positions.keys(), reverse=True):
        positions = file_positions[file_id]
        file_length = len(positions)

        for i in range(n - file_length + 1):
            if i > positions[0]:
                break
            if all(block == "." for block in blocks[i : i + file_length]):
                for pos in positions:
                    blocks[pos] = "."
                for j in range(file_length):
                    blocks[i + j] = file_id
                break

    return blocks


def part2(blocks):
    compacted_blocks = compact_disk_whole_files(blocks)
    checksum = calculate_checksum(compacted_blocks)
    return checksum


def main():
    input_file = "input/day9.txt"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    with open(input_file) as f:
        blocks = parse_disk_map(f.read().strip())
    print(part1(blocks[:]))
    print(part2(blocks))


if __name__ == "__main__":
    main()
