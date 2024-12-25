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


def find_min_distances(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int], debug = False) -> list[list[list[int]]]:
    rows, cols = len(grid), len(grid[0])
    seen = [[[math.inf] * 4 for _ in range(cols)] for _ in range(rows)]
    
    dir_dict = {(0, 1): 0, (1,0): 1, (0, -1): 2, (-1, 0): 3}
    
    queue = [(0, start, (0, 1))]
    best_score = math.inf
    
    while queue and queue[0][0] <= best_score:
        if debug:
            print(queue)
        points, pos, dir = heapq.heappop(queue)
        
        if seen[pos[0]][pos[1]][dir_dict[dir]] != math.inf:
            continue
        seen[pos[0]][pos[1]][dir_dict[dir]] = points
        
        if grid[pos[0]][pos[1]] == END:
            print(points)
            best_score = points
            continue
        
        # rotations
        if seen[pos[0]][pos[1]][dir_dict[(dir[1], dir[0])]] == math.inf:
            heapq.heappush(queue, (points + 1000, pos , (dir[1], dir[0])))
        
        if seen[pos[0]][pos[1]][dir_dict[(-dir[1], -dir[0])]] == math.inf:
            heapq.heappush(queue, (points + 1000, pos , (- dir[1], - dir[0])))

        # move forward
        new = (pos[0] + dir[0], pos[1] + dir[1]) # no rotation
        if grid[new[0]][new[1]] != WALL and seen[new[0]][new[1]][dir_dict[dir]] == math.inf:
            heapq.heappush(queue, (points + 1, new, dir))
    
    return seen


def find_path_tiles(seen: list[list[list[int]]], end: tuple[int, int]) -> int:
    # print(seen[end[0]][end[1]])
    stack = [(end, points, i) for i, points in enumerate(seen[end[0]][end[1]]) if points != math.inf]
    
    dir_dict = [(0, 1), (1,0), (0, -1), (-1, 0)]
    
    # returns the 3 possible previous directions from a direction
    all_pos = lambda x: [(x, -1), ((x - 1) % 4, -1001), ((x + 1) % 4, -1001)]
    
    tiles = set()
    
    while stack:
        # print(stack)
        cur_pos, points, dir = stack.pop()
        
        tiles.add(cur_pos)
        
        for new_dir, d_points in all_pos(dir):
            nx = cur_pos[0] - dir_dict[new_dir][0]
            ny = cur_pos[1] - dir_dict[new_dir][1]
            np = points + d_points
            # print(seen[nx][ny])
            if seen[nx][ny][new_dir] == np:
                stack.append(((nx, ny), np, new_dir))
    
    print(sorted(list(tiles)))
    return len(tiles)
    

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
    
    min_distances = find_min_distances(grid, start, end, debug)
    path_spots = find_path_tiles(min_distances, end)
    print(path_spots)


if __name__ == "__main__":
    
    # Argument parsing for debugging and directory inputs
    parser = argparse.ArgumentParser(
        prog="Find Best Tiles day 16 part 2",
        description="""Advent of Code, day 16 part 2, finds the amount of tiles
        that are used by one of the best paths through grid given in directory"""
    )
    parser.add_argument("-d", "--directory", default=DIR)
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    args = parser.parse_args()
    
    main(args.verbose, args.directory)
    