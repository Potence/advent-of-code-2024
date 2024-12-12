

def read_all(directory: str) -> list[list[int]]:
    res = []
    
    with open(directory, 'r') as f:
        for line in f:
            res.append(list(line.strip()))
    
    return res
    

def search(grid: list[list[int]], position: tuple[int, int], direction: tuple[int, int]) -> bool:
    cur = [position[0], position[1]]
    for char in "XMAS":
        if not (0 <= cur[0] < len(grid)) or not (0 <= cur[1] < len(grid[0])):
            return False
        if char != grid[cur[0]][cur[1]]:
            return False
        cur[0] += direction[0]
        cur[1] += direction[1]
    
    return True
    

def search_all(grid: list[list[int]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # print(i, j)
            if grid[i][j] == 'X':
                count += search(grid, (i,j), (1,1))
                count += search(grid, (i,j), (1,0))
                count += search(grid, (i,j), (1,-1))
                count += search(grid, (i,j), (0,1))
                count += search(grid, (i,j), (0,-1))
                count += search(grid, (i,j), (-1,1))
                count += search(grid, (i,j), (-1,0))
                count += search(grid, (i,j), (-1,-1))

    return count
    

if __name__ == "__main__":
    data_directory = r"D:\advent-of-code\day4\data.txt"
    grid = read_all(data_directory)
    res = search_all(grid)
    print(res)
    