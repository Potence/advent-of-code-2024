

def main(directory: str):
    total = 0
    
    with open(directory, 'r') as f:
        mul, do = False, True
        prev = ""
        cur = f.read(1)
        while cur:
            prev += cur
            
            if prev == "mul(":
                nums = [""]
                for i in range(8):
                    cur = f.read(1)
                    if cur.isdigit():
                        nums[-1] += cur
                    elif cur == ',':
                        nums.append("")
                    elif cur == ')' and len(nums) >= 2:
                        mul = True
                        break
                    else:
                        break
                if mul:
                    mul = False
                    # print(nums)
                    if do:
                        total += int(nums[0]) * int(nums[1])
                prev = cur
            elif prev == "don't()":
                do = False
            elif prev == "do()":
                do = True
            
            if not (prev == "mul("[:len(prev)] or prev == "don't()"[:len(prev)] or prev == "do()"[:len(prev)]):
                prev = cur
            cur = f.read(1)
            
    print(total)


if __name__ == "__main__":
    main(r"D:\advent-of-code\day3\data.txt")
