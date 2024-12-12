from part1 import read_all
from collections import Counter


def get_similarity(list1: list[int], list2: list[int]) -> int:
    list2_counts = Counter(list2)
    similarity = 0
    
    for num in list1:
        similarity += num * list2_counts[num]
    
    return similarity


def main():
    input_directory = r"D:\advent-of-code\day1\imput.txt"
    list1, list2 = read_all(input_directory)
    similarity_score = get_similarity(list1, list2)
    print(similarity_score)

if __name__ == "__main__":
    main()
    