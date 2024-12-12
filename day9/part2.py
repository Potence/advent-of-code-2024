from dataclasses import dataclass
DIR = r"D:\advent-of-code\day9\data.txt"



@dataclass
class Block:
    index: int = -1
    length: int = 0

def decompress(compressed_data: str) -> list[int|None]:
    data = []
    for i, c in enumerate(compressed_data):
        if int(i) % 2 == 0:
            data += [i // 2] * int(c)
        else:
            data += [None] * int(c)
    return data


def reformat_data(data: list[int|None], empty_blocks: list[Block]) -> list[int]:
    print(data)
    l, r = 0, len(data) - 1
    
    last_block =-1
    
    while l < r:
        # if data[l] != None:
        #     l += 1
        if data[r] != None: 
            # found a block
            cur_block = data[r]
            cur_block_len = 0
            while data[r] == cur_block:
                r -= 1
                cur_block_len += 1
            
            for i, block in enumerate(empty_blocks):
                if block.index > r:
                    break
                if block.length >= cur_block_len:
                    # move block
                    data[block.index: block.index + cur_block_len] = [cur_block] * cur_block_len
                    data[r + 1: r + 1 + cur_block_len] = [None] * cur_block_len
                    # update empty blocks
                    if cur_block_len != block.length:
                        empty_blocks[i] = Block(block.index + cur_block_len, block.length - cur_block_len)
                    else:
                        empty_blocks.pop(i)
                    break
                
            # print([f'{x}' if type(x) == int else '.' for x in data], cur_block, cur_block_len)
        elif data[r] == None:
            # still in empty space
            r -= 1
    
    return data


def indicies_of_empty_block(compressed_data: str) -> list[Block]:
    blocks = []
    cur_index = 0
    for i, b in enumerate(compressed_data):
        if i % 2 == 1 and b != "0":
            blocks.append(Block(cur_index, int(b)))
        cur_index += int(b)
    return blocks
        

def checksum(data: list[int]) -> int:
    total = 0
    for i, num in enumerate(data):
        if num is not None:
            total += i * num
    return total
    

def main(directory: str = DIR):
    compressed_data = ""
    with open(directory, 'r') as f:
        compressed_data = f.readline().strip()
    
    decompressed_data = decompress(compressed_data)
    empty_blocks = indicies_of_empty_block(compressed_data)
    print(empty_blocks)
    # print(decompressed_data)
    data = reformat_data(decompressed_data, empty_blocks)
    # print(data)
    print(checksum(data))
    return
    

if __name__ == "__main__":
    main()
