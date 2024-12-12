from collections import defaultdict

DIR = r"D:\advent-of-code\day5\test_data.txt"


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


def is_invalid_order(order: list[int], rules: dict[int: set[int]]) -> None|tuple[int,int]:
    nums_in_row = set(order)
    seen = set()
    
    def no_conflict_index(order: list[int])
    
    for i, num in enumerate(order):
        cur = nums_in_row.intersection(rules[num]).difference(seen)
        if len(cur) > 0:
            temp = (i, order.index(cur.pop()))
            print(temp)
            return temp
        seen.add(num)
    
    return None


def main():
    rules, line = read_rules(DIR)
    orders = read_orders(DIR, line)
    print(dict(rules))
    total = 0
    
    for i, order in enumerate(orders):
        cur = is_invalid_order(order, rules)
        if cur is not None:
            order[cur[0]], order[cur[1]] = order[cur[1]], order[cur[0]]
            print(order)
            total += order[len(order) // 2]
            # print(i)
            # print(order[len(order) // 2])
    
    print(total)


if __name__ == "__main__":
    main()
    