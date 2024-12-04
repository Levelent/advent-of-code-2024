import itertools

def get_grid() -> list[str]:
    with open("in.txt") as file:
        lines = file.read().split("\n")

    if lines[-1] == "":
        lines = lines[:-1]
    
    return lines

def part_a(grid: list[str]) -> int:
    # Looking for XMAS (any rotation)
    total = 0
    search_str = "XMAS"

    for y, x in itertools.product(range(len(grid)), range(len(grid[0]))):
        if grid[y][x] != search_str[0]:
            continue

        # all cardinal directions of movement (+ stationary, but doesn't matter here)
        for step_x, step_y in itertools.product([-1, 0, 1], [-1, 0, 1]):

            # ensure we don't index out of bounds
            if not (0 <= y + step_y * (len(search_str) - 1) <= len(grid) - 1):
                continue
            if not (0 <= x + step_x * (len(search_str) - 1) <= len(grid[0]) - 1):
                continue

            total += search_str == "".join(
                grid[y + step_y * i][x + step_x * i] for i in range(len(search_str))
            )

    return total

def part_b(grid: list[str]) -> int:
    # Looking for
    # M.S
    # .A.
    # M.S
    # (any rotation)
    total = 0

    for y, x in itertools.product(range(len(grid)), range(len(grid[0]))):
        # center the 3x3 box on A
        if grid[y][x] != "A":
            continue

        num_found = 0
        
        for step_x, step_y in itertools.product([-1, 1], [-1, 1]):  # only check diagonals

            # avoid iterating out of bounds - A cannot be on grid edge
            if not (1 <= y <= len(grid) - 2) or not (1 <= x <= len(grid[0]) - 2):
                continue

            num_found += "MAS" == "".join(
                grid[y + step_y * i][x + step_x * i] for i in range(-1, 2)
            )
        
        # 3x3 box equivalent to finding two diagonal MAS
        if num_found > 1:
            total += 1

    return total

if __name__ == "__main__":
    grid = get_grid()
    print(part_a(grid))
    print(part_b(grid))
