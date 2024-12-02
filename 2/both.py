def get_lists() -> list[list[int]]:
    with open("in.txt") as file:
        lines = file.read().split("\n")

    if lines[-1] == "":
        lines = lines[:-1]
    
    return [[int(num) for num in line.split()] for line in lines]

def test_row(row: list[int]) -> bool:
    # if strictly increasing or decreasing by 1-3
    diffs = [row[i] - row[i+1] for i in range(len(row)-1)]
    is_increasing = True
    is_decreasing = True
    for diff in diffs:
        is_increasing &= 1 <= diff <= 3
        is_decreasing &= -3 <= diff <= -1
    return is_increasing or is_decreasing

def test_tolerance_row(row: list[int]) -> bool:
    # allow removal of up to 1 element
    if test_row(row):
        return True
    
    for i in range(len(row)):
        if test_row(row[:i] + row[i+1:]):
            return True
    
    return False

def part_a(num_grid: list[list[int]]) -> int:
    return sum(test_row(row) for row in num_grid)

def part_b(num_grid: list[list[int]]) -> int:
    return sum(test_tolerance_row(row) for row in num_grid)

if __name__ == "__main__":
    num_grid = get_lists()
    print(part_a(num_grid))
    print(part_b(num_grid))
