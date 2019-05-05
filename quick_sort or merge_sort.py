import random

def sort(list):
    if len(list) == 0 or len(list) == 1: return list
    pivot = random.randint(0, len(list) - 1)
    sublist = []
    i = 0
    for x in list:
        if x < list[pivot]:
            sublist.insert(i, x)
            i += 1
        else:
            sublist.append(x)
    if len(sublist) >= 2:
        return sort(sublist[:i]) + sort(sublist[i:])
    else:
        return sublist

# example = [4, 3, 2, 5, 6, 1, 0]
# print(sort(example))