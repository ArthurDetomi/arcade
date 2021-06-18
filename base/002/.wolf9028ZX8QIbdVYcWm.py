from typing import List

def fit(line: List[str], index: int, value: int, prox: int): 
    left = line[max(0, index - prox) : index]
    right = line[index + 1: min(index + prox + 1, len(line))]
    return str(value) not in (left + right)

def find_next(line: List[str], index):
    return "".join(line).find(".", index + 1)

def solver(line: List[str], index: int, lim: int, prox: int) -> bool:
    if(index == -1):
        #print("".join(line) + " <----")
        return True
    for v in range(lim + 1):
        if fit(line, index, v, prox):
            line[index] = str(v)
            #print("".join(line))
            new_index = find_next(line, index)
            if solver(line, new_index, lim, prox):
                return True
    line[index] = "."
    #print("".join(line))
    return False


    
line = input()
line = [c for c in line]
prox = int(input())

for lim in range(1, 10):
    if solver(line, 0, lim, prox):
        print(lim)
        break
