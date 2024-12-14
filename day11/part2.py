from functools import cache

DIR = r"D:\advent-of-code\day11\data.txt"
BLINKS = 75


def read_stones(dir: str=DIR) -> list[int]:
    res = []
    
    with open(dir, "r") as f:
        line = f.readline()
        res = [int(x) for x in line.split(" ")]
    
    return res


@cache
def blink(stone: int, days_left: int) -> int:
    if days_left == 0: return 1
    if stone == 0: return blink(1, days_left - 1)
    
    length = len(str(stone))
    if length % 2 == 0:
        return blink(int(str(stone)[:length // 2]), days_left - 1) + \
            blink(int(str(stone)[length // 2:]), days_left - 1)
    return blink(2024 * stone, days_left - 1)


def stones_after_n_blinks(initial_stones: list[int], n: int=BLINKS) -> int:
    total = 0
    for stone in initial_stones:
        total += blink(stone, BLINKS)
    
    return total


def main():
    stones = read_stones()
    print(stones)
    total_stones = stones_after_n_blinks(stones)
    print(total_stones)
    return


if __name__ == "__main__":
    main()
    