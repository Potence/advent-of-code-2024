from collections import defaultdict

DIR = r"D:\advent-of-code\day8\data.txt"


def read_graph(directory: str = DIR) -> list[list[str]]:
    res = []
    
    with open(directory, "r") as f:
        for line in f:
            res.append([x for x in line if x != "\n"])
    
    return res


def find_nodes_in_graph(graph: list[list[str]]) -> dict[str: list[tuple[int, int]]]:
    nodes = defaultdict(list)
    
    for i, row in enumerate(graph):
        for j, pos in enumerate(row):
            if pos != ".":
                nodes[pos].append((i, j))
    
    return nodes


def find_anti_nodes(positions: list[tuple[int, int]], rows: int, cols: int) -> int:
    anti_nodes = []
    
    for i, pos1 in enumerate(positions):
        for pos2 in positions[i + 1:]:
            dist = (pos2[0] - pos1[0], pos2[1] - pos1[1])
            
            new1 = pos1
            new2 = pos2
            
            while 0 <= new1[0] < rows and 0 <= new1[1] < cols:
                anti_nodes.append(new1)
                new1 = (new1[0] - dist[0], new1[1] - dist[1])
                
            while 0 <= new2[0] < rows and 0 <= new2[1] < cols:
                anti_nodes.append(new2)
                new2 = (new2[0] + dist[0], new2[1] + dist[1])

    return anti_nodes


def main():
    graph = read_graph()
    rows, cols = len(graph), len(graph[0])
    nodes = find_nodes_in_graph(graph)
    anti_nodes = set()
    
    for positons in nodes.values():
        new_anti_nodes = find_anti_nodes(positons, rows, cols)
        anti_nodes.update(new_anti_nodes)
    
    print(len(anti_nodes))
    return


if __name__ == "__main__":
    main()
    