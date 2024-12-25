import math
from collections import deque
import heapq
import argparse

DIR = r"D:\advent-of-code\day16\data.txt"
WALL = "#"
END = "E"


def read_grid(directory: str = DIR) -> list[list[str]]:
    res = []
    with open(directory, "r") as f:
        for line in f:
            res.append([c for c in line.strip()])
    return res


def find_min_distance(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int], debug = False) -> int:
    rows, cols = len(grid), len(grid[0])
    seen = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]
    
    dir_dict = {(0, 1): 0, (1,0): 1, (0, -1): 2, (-1, 0): 3}
    
    queue = [(0, start, (0, 1))]
    
    while queue:
        if debug:
            print(queue)
        points, pos, dir = heapq.heappop(queue)
        
        if seen[pos[0]][pos[1]][dir_dict[dir]]:
            continue
        seen[pos[0]][pos[1]][dir_dict[dir]] = True
        
        if grid[pos[0]][pos[1]] == END:
            return points
        
        # clockwise rotation
        new = (pos[0] + dir[1], pos[1] + dir[0])
        if grid[new[0]][new[1]] != WALL and not seen[new[0]][new[1]][dir_dict[(dir[1], dir[0])]]:
            heapq.heappush(queue, (points + 1001, new , (dir[1], dir[0])))
        
        # counter-clockwise rotation
        new = (pos[0] - dir[1], pos[1] - dir[0])
        if grid[new[0]][new[1]] != WALL and not seen[new[0]][new[1]][dir_dict[(-dir[1], -dir[0])]]:
            heapq.heappush(queue, (points + 1001, new , (- dir[1], - dir[0])))

        # no rotation
        new = (pos[0] + dir[0], pos[1] + dir[1]) 
        if grid[new[0]][new[1]] != WALL and not seen[new[0]][new[1]][dir_dict[dir]]:
            heapq.heappush(queue, (points + 1, new, dir))
    
    return math.inf


def main(debug = False, dir = DIR):
    grid = read_grid(dir)
    
    # find start and end position
    start, end = None, None
    for i, line in enumerate(grid):
        if "S" in line:
            start = (i, line.index("S"))
        if "E" in line:
            end = (i, line.index("E"))
    
    if not start or not end:
        raise Exception(f"start={start} or end={end}")
    
    if debug:
        print(start, end)
    
    min_distance = find_min_distance(grid, start, end, debug)
    print(min_distance)


if __name__ == "__main__":
    
    # Argument parsing for debugging and directory inputs
    parser = argparse.ArgumentParser(
        prog="Find Best Tiles day 16 part 1",
        description="""Advent of Code day 16 part 1, finds the amount of tiles
        that are used by one of the best paths through grid given in directory"""
    )
    parser.add_argument("-d", "--directory", default=DIR)
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    args = parser.parse_args()
    
    main(args.verbose, args.directory)
    
    