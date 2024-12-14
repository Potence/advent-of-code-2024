# constants
DIR = r"D:\advent-of-code\day10\data.txt"


def read_graph(dir: str) -> list[list[int]]:
    graph = []
    with open(dir, "r") as f:
        for line in f:
            graph.append([int(x) for x in line if x.isdigit()])
    return graph


def dfs(graph, row, col, seen=set(), nines=set()) -> set:
    seen.add((row, col))
    # end case
    if graph[row][col] == 9:
        nines.add((row, col))
        return nines
    
    if row + 1 < len(graph) and graph[row + 1][col] == graph[row][col] + 1:
        nines.update(dfs(graph, row + 1, col, seen, nines))
    if col + 1 < len(graph[0]) and graph[row][col + 1] == graph[row][col] + 1:
        nines.update(dfs(graph, row, col + 1, seen, nines))
    if row - 1 >= 0 and graph[row - 1][col] == graph[row][col] + 1:
        nines.update(dfs(graph, row - 1, col, seen, nines))
    if col - 1 >= 0 and graph[row][col - 1] == graph[row][col] + 1:
        nines.update(dfs(graph, row, col - 1, seen, nines))
        
    return nines


def find_all_trails(graph: list[list[int]]) -> list[int]:
    """
    Find all trailhead (graphs with a start heigh of 0) and return all trails
    scores which is how many max altitude positions it can reach (by 
    travering the graph in up, right, down, and left directions and strictly
    going up by 1 height in each move)
    """
    result = []
    n_rows, n_cols = len(graph), len(graph[0])
    for i in range(n_rows):
        for j in range(n_cols):
            if graph[i][j] == 0:
                a = dfs(graph, row=i, col=j, seen=set(), nines=set())
                # print(a)
                result.append(len(a))

    return result


def main():
    graph = read_graph(DIR)
    res = find_all_trails(graph)
    print(res)
    print(sum(res))
    

if __name__ == "__main__":
    main()