DIR = r"D:\advent-of-code\day7\data.txt"

def read_equations(directory: str = DIR) -> list[list[int]]:
    res = []
    
    with open(directory, "r") as f:
        for line in f:
            line = line.split(":")
            res.append([int(line[0])] + [int(x) for x in line[1].split()])

    return res


def can_equate(target: int, equation: list[int]) -> bool:
    def next(i: int, cur: int):
        if i >= len(equation) - 1:
            if cur == target:
                return True
            else:
                return False
        a = next(i + 1, cur + equation[i + 1])
        b = next(i + 1, cur * equation[i + 1])
        return a or b
    
    return next(0, equation[0])
        

def main():
    equations = read_equations()
    calibration = 0
    
    for equation in equations:
        if can_equate(equation[0], equation[1:]):
            calibration += equation[0]
    
    print(calibration)


if __name__ == "__main__":
    main()
    