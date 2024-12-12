

def read_all(dir: str) -> list[list[int]]:
    """Read both lists from directory file where lists are seperated by spaces
    and entries by line and return both lists as integer lists.

    Args:
        dir (str): file directory of file containing both lists

    Returns:
        list[list[int]]: list containing list 1 and list 2
    """
    res = [[], []]
    with open(dir) as f:
        for cur in f:
            l1, l2 = cur.split()
            res[0].append(int(l1))
            res[1].append(int(l2))
    return res

def get_total_distance(list1: list[int], list2: list[int]) -> int:
    """sort both lists and pair sortednus in list1 with list2 and return the
    total of absolute differences between pairs of numbers

    Args:
        list1 (list[int]): list of numbers
        list2 (list[int]): list of numbers

    Returns:
        int: total distance between the 2 lists
    """
    list1.sort()
    list2.sort()
    dist = 0
    
    for n1, n2 in zip(list1, list2):
        dist += abs(n1 - n2)
    
    return dist


def main():
    input_directory = r"D:\advent-of-code\day1\imput.txt"
    l1, l2 = read_all(input_directory)
    dist = get_total_distance(l1, l2)
    print(dist)


if __name__=="__main__":
    main()