def get_text() -> str:
    with open("in.txt") as file:
        return file.read()
    
def try_parse_mul(text: str) -> int:
    # want format mul(123,456) [no spaces, 1-3 digit numbers]
    if text[:4] != "mul(":
        return 0
    
    remaining = text[4:]
    
    # chop off at first )
    idx = remaining.find(")")
    if idx == -1:
        return 0
    remaining = remaining[:idx]

    # no spaces
    if remaining.find(" ") != -1:
        return 0

    args: list[str] = remaining.split(",")
    if len(args) != 2:
        return 0
    
    # must be ints
    for arg in args:
        if not arg.isdigit():
            return 0

    return int(args[0]) * int(args[1])

def part_a(text: str) -> int:
    total = 0

    for pos in range(len(text)):
        total += try_parse_mul(text[pos:])
    
    return total

def part_b(text: str) -> int:
    total = 0
    enabled = True

    for pos in range(len(text)):
        if text[pos:].startswith("do()"):
            enabled = True
        elif text[pos:].startswith("don't()"):
            enabled = False
        elif enabled:
            total += try_parse_mul(text[pos:])
    
    return total


if __name__ == "__main__":
    text = get_text()
    print(part_a(text))
    print(part_b(text))