import re
from collections import deque

DIR = r"D:\advent-of-code\day18\data.txt"
SIZE = 70 + 1
CORRUPTED_COUNT = 1024


def read_bytes(directory: str = DIR) -> list[list[int]]:
    res = []
    
    with open(directory, "r") as f:
        for i, line in enumerate(f):
            if i == CORRUPTED_COUNT:
                break
            res.append([int(x) for x in re.findall("\d+", line)])
            
    return res


def best_path_len(corrupted_bytes: list[list[int]]) -> int:
    grid = [[True] * SIZE for _ in range(SIZE)] # true if uncorrupted, or unexplored
    
    # fill in corrupted bytes
    for x, y in corrupted_bytes:
        grid[y][x] = False
    
    queue = deque([(0, 0, 0)])
    
    while queue:
        cur_steps, cur_x, cur_y = queue.popleft()
        
        if grid[cur_y][cur_x] == False:
            continue
        grid[cur_y][cur_x] = False
        
        if cur_x == SIZE - 1 and cur_y == SIZE - 1:
            return cur_steps
        
        for dx, dy in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cur_x + dx, cur_y + dy
            
            if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx]:
                queue.append((cur_steps + 1, nx, ny))
    
    return -1


def main():
    corrupted_bytes = read_bytes(DIR)
    length = best_path_len(corrupted_bytes)
    print(length)


if __name__ == "__main__":
    main()
