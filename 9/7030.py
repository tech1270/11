with open("7030") as file:
    data = [list(map(int, item.split())) for item in file]
    result = 0
    for item in data:
        duplicates = set([x for x in item if item.count(x) == 2])
        if len(duplicates) == 3:
            a, b, c = sorted(list(duplicates))
            if a ** 2 + b ** 2 == c ** 2:
                result += 1
    print(result)
