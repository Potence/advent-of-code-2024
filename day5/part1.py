from collections import defaultdict

DIR = r"D:\advent-of-code\day5\data.txt"


def read_rules(directory: str) -> tuple[dict[int: set[int]], int]:
    rules = defaultdict(set)
    orders_start = -1
    
    with open(directory, "r") as f:
        for i, row in enumerate(f):
            if row == "\n":
                orders_start = i
                break
            pre, post = row[:-1].split('|')
            rules[int(post)].add(int(pre))
    
    return rules, orders_start
            

def read_orders(directory: str, start_line: int) -> list[list[int]]:
    orders = []
    
    with open(directory, "r") as f:
        for _ in range(start_line + 1):
            f.readline()
        
        cur = f.readline().strip()
        
        while cur:
            orders.append([int(x) for x in cur.split(',')])
            cur = f.readline().strip()
    
    return orders


def is_valid_order(order: list[int], rules: dict[int: set[int]]) -> bool:
    nums_in_row = set(order)
    seen = set()
    
    for num in order:
        if len(seen.difference(nums_in_row.intersection(rules[num]))) > 0:
            return False
        seen.add(num)
    
    return True


def main():
    rules, line = read_rules(DIR)
    orders = read_orders(DIR, line)
    total = 0
    
    for i, order in enumerate(orders):
        if is_valid_order(order, rules):
            total += order[len(order) // 2]
            # print(i)
            # print(order[len(order) // 2])
    
    print(total)


if __name__ == "__main__":
    main()
    