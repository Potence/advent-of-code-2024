

def read_all(directory: str) -> list[list[int]]:
    res = []
    
    with open(directory, 'r') as f:
        for line in f:
            res.append(list(line.strip()))
    
    return res
    

def search(grid: list[list[int]], position: tuple[int, int]) -> bool:
    if not (1 <= position[0] < len(grid) - 1) or not (1 <= position[1] < len(grid[0]) - 1):
        return False
    
    if grid[position[0] + 1][position[1] + 1] == grid[position[0] + 1][position[1] - 1] == "M" and \
        grid[position[0] - 1][position[1] + 1] == grid[position[0] - 1][position[1] - 1] == "S":
        # print(position)
        return True
    elif grid[position[0] - 1][position[1] + 1] == grid[position[0] - 1][position[1] - 1] == "M" and \
        grid[position[0] + 1][position[1] + 1] == grid[position[0] + 1][position[1] - 1] == "S":
        # print(position)
        return True
    elif grid[position[0] + 1][position[1] + 1] == grid[position[0] - 1][position[1] + 1] == "M" and \
        grid[position[0] + 1][position[1] - 1] == grid[position[0] - 1][position[1] - 1] == "S":
        # print(position)
        return True
    elif grid[position[0] + 1][position[1] - 1] == grid[position[0] - 1][position[1] - 1] == "M" and \
        grid[position[0] + 1][position[1] + 1] == grid[position[0] - 1][position[1] + 1] == "S":
        # print(position)
        return True
    
    return False
    

def search_all(grid: list[list[int]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # print(i, j)
            if grid[i][j] == 'A':
                count += search(grid, (i,j))

    return count
    

if __name__ == "__main__":
    data_directory = r"D:\advent-of-code\day4\data.txt"
    grid = read_all(data_directory)
    res = search_all(grid)
    print(res)
    