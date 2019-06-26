
def sort(list):
    for x in range(len(list) - 1, 0, -1):
        for i in range(x):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


example = [4, 2, 3, 0, 5, 6, 1]
print(sort(example))
