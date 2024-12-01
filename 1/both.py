from collections import Counter

def get_sorted_lists() -> tuple[list[int], list[int]]:
    with open("in.txt") as file:
        lines = file.read().split("\n")

    if lines[-1] == "":
        lines = lines[:-1]
    
    list_a = []
    list_b = []
    for line in lines:
        a_str, b_str = line.split("   ")
        list_a.append(int(a_str))
        list_b.append(int(b_str))

    list_a.sort()
    list_b.sort()

    return list_a, list_b

def part_a(list_a: list[int], list_b: list[int]) -> int:
    # Difference sum of sorted
    total = 0
    for i in range(len(list_a)):
        total += abs(list_a[i] - list_b[i])
    
    return total


def part_b(list_a: list[int], list_b: list[int]) -> int:
    # Sum of (elem * frequency in a * frequency in b)
    counter_a = Counter(list_a)
    counter_b = Counter(list_b)

    total = 0
    for elem, cnt in counter_a.items():
        total += elem * cnt * counter_b[elem]
    
    return total

if __name__ == "__main__":
    list_a, list_b = get_sorted_lists()
    print(part_a(list_a, list_b))
    print(part_b(list_a, list_b))
