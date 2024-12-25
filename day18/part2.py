import re
from collections import deque

DIR = r"D:\advent-of-code\day18\data.txt"
SIZE = 70 + 1
CORRUPTED_COUNT = -1 # read all corrupted bytes


def read_bytes(directory: str = DIR) -> list[list[int]]:
    res = []
    
    with open(directory, "r") as f:
        for i, line in enumerate(f):
            if i == CORRUPTED_COUNT:
                break
            res.append([int(x) for x in re.findall("\d+", line)])
            
    return res


def can_reach_end(corrupted_bytes: list[list[int]]) -> bool:
    grid = [[True] * SIZE for _ in range(SIZE)] # true if uncorrupted, or unexplored
    
    # fill in corrupted bytes
    for x, y in corrupted_bytes:
        grid[y][x] = False
    
    queue = deque([(0, 0)])
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        if grid[cur_y][cur_x] == False:
            continue
        grid[cur_y][cur_x] = False
        
        if cur_x == SIZE - 1 and cur_y == SIZE - 1:
            return True
        
        for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cur_x + dx, cur_y + dy
            
            if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx]:
                queue.append((nx, ny))
    
    return False


def bin_search_corrupted(corrupted_bytes: list[list[int]]) -> int:
    l, r = 0, len(corrupted_bytes)
    
    while l < r:
        mid = l + (r - l) // 2
        if can_reach_end(corrupted_bytes[:mid]):
            # print(f"can do {mid}")
            l = mid + 1
        else:
            # print(f"can't do {mid}")
            r = mid
        # input(f"{l}, {r}")
    
    return l - 1


def main():
    corrupted_bytes = read_bytes(DIR)
    max_bytes = bin_search_corrupted(corrupted_bytes)
    print(max_bytes)
    print(corrupted_bytes[max_bytes])


if __name__ == "__main__":
    main()
