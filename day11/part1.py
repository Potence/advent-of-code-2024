DIR = r"D:\advent-of-code\day11\test_data.txt"
BLINKS = 25


def read_stones(dir: str=DIR) -> list[int]:
    res = []
    
    with open(dir, "r") as f:
        line = f.readline()
        res = [int(x) for x in line.split(" ")]
    
    return res


def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        length = len(str(stone))
        if stone == 0:
            new_stones.append(1)
        elif length % 2 == 0:
            new_stones.append(int(str(stone)[:length // 2]))
            new_stones.append(int(str(stone)[length // 2:]))
        else:
            new_stones.append(2024 * stone)
    return new_stones


def perform_n_blinks(initial_stones: list[int], n: int=BLINKS) -> list[int]:
    stones = initial_stones
    for _ in range(n):
        stones = blink(stones)
    return stones


def main():
    stones = read_stones()
    stones = perform_n_blinks(stones)
    print(len(stones))
    return


if __name__ == "__main__":
    main()
    