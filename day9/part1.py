
DIR = r"D:\advent-of-code\day9\data.txt"


def decompress(compressed_data: str) -> list[int|None]:
    data = []
    for i, c in enumerate(compressed_data):
        if int(i) % 2 == 0:
            data += [i // 2] * int(c)
        else:
            data += [None] * int(c)
    return data


def reformat_data(data: list[int|None]) -> list[int]:
    l, r = 0, len(data) - 1
    
    while l < r:
        if data[l] != None:
            l += 1
        elif data[r] == None:
            r -= 1
        else: 
            data[l] = data[r]
            l += 1
            r -= 1
    
    return data[:l + 1]


def checksum(data: list[int]) -> int:
    total = 0
    for i, num in enumerate(data):
        total += i * num
    return total
    

def main(directory: str = DIR):
    compressed_data = ""
    with open(directory, 'r') as f:
        compressed_data = f.readline().strip()
        
    decompressed_data = decompress(compressed_data)
    # print(decompressed_data)
    data = reformat_data(decompressed_data)
    # print(data)
    print(checksum(data))
    return
    

if __name__ == "__main__":
    main()
