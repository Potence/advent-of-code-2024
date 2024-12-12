
DIR = r"D:\advent-of-code\day6\data.txt"


def read_grid(directory: str= DIR) -> tuple[list[list[int]], tuple[int,int]]:
    grid = []
    start = None
    
    with open(directory, "r") as f:
        for i, line in enumerate(f):
            grid.append([c for c in line])
            if "^" in line:
                start = (i, line.index('^'))
                
    return grid, start


def find_path(grid: list[list[int]], start: tuple[int,int]) -> int:
    direction = (-1, 0)
    cur = start
    unique_positions = 0
    
    while 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]):
        if grid[cur[0]][cur[1]] != 'X':
            grid[cur[0]][cur[1]] = 'X'
            unique_positions += 1
        new = (cur[0] + direction[0], cur[1] + direction[1])
        if 0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0]) and grid[new[0]][new[1]] == '#':
            direction = (1 * direction[1],-1 * direction[0])
        else:
            cur = new
    
    return unique_positions
    

def main():
    grid, start_pos = read_grid(DIR)
    unique_positions = find_path(grid, start_pos)
    print(unique_positions)
    return


if __name__ == "__main__":
    main()
    