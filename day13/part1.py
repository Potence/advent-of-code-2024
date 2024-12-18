from functools import cache
import math
DIR = r"D:\advent-of-code\day13\data.txt"


def get_machine_input(file) -> list[list[int, int]]:
    try:
        res = []
        cur = file.readline()
        res.append([int(cur[12:14]), int(cur[18:20])])
        cur = file.readline()
        res.append([int(cur[12:14]), int(cur[18:20])])
        cur = file.readline()
        cur = cur.strip()
        cur = cur.split(",")
        res.append([int(cur[0].split("=")[-1]), int(cur[1].split("=")[-1])])
        file.readline()
        return res
    except:
        return []
        

def tokens_to_reach(A: tuple[int, int], B: tuple[int, int], target: tuple[int, int]):
    
    @cache
    def min_to_reach(cur_target: tuple[int, int], cur_tokens: int, cur_a: int, cur_b: int):
        if cur_a > 100 or cur_b > 100 or cur_target[0] < 0 or cur_target[1] < 0:
            return math.inf
        if cur_target == (0, 0):
            return cur_tokens
        
        a_cost = min_to_reach((cur_target[0] - A[0], cur_target[1] - A[1]), cur_tokens + 3, cur_a + 1, cur_b)
        b_cost = min_to_reach((cur_target[0] - B[0], cur_target[1] - B[1]), cur_tokens + 1, cur_a, cur_b + 1)
        
        return min(a_cost, b_cost)
    
    res = min_to_reach(tuple(target), 0, 0, 0)
    if res != math.inf:
        return res
    return 0


def main():
    tokens = 0
    
    with open(DIR, "r") as f:
        while f.readable():
            next_inp = get_machine_input(f)
            if next_inp == []:
                break
            tokens += tokens_to_reach(next_inp[0], next_inp[1], next_inp[2])
    
    print(tokens)


if __name__ == "__main__":
    main()
