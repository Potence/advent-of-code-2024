import numpy as np

# sys.setrecursionlimit(4000)

DIR = r"/mnt/d/advent-of-code/day13/data.txt"


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
        res.append([int(cur[0].split("=")[-1]) + 10000000000000, int(cur[1].split("=")[-1]) + 10000000000000])
        file.readline()
        return res
    except:
        return []
        

def tokens_to_reach3(A: tuple[int, int], B: tuple[int, int], target: tuple[int, int]):
    M = np.array([[A[0], B[0]], [A[1], B[1]]])
    P = np.array([target[0], target[1]])
    R = np.round(np.linalg.solve(M, P))
    return int(R@(3,1)) if (P==R@M.T).all() else 0


def tokens_to_reach4(A: tuple[int, int], B: tuple[int, int], target: tuple[int, int]):
    b_count = int((A[0] * target[1] - A[1] * target[0]) / (A[0] * B[1] - A[1] * B[0]))
    a_count = int((target[0] - B[0] * b_count) / A[0])
    
    if A[0] * a_count + B[0] * b_count == target[0] and \
        A[1] * a_count + B[1] * b_count == target[1]:
        return a_count * 3 + b_count
    return 0


def main():
    tokens = 0
    b_tokens = 0
    
    with open(DIR, "r") as f:
        while f.readable():
            next_inp = get_machine_input(f)
            if next_inp == []:
                break
            tokens += tokens_to_reach3(next_inp[0], next_inp[1], next_inp[2])
    
    print(tokens)


if __name__ == "__main__":
    main()
