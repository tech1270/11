with open("7674") as file:
    data = [list(map(int, item.split())) for item in file]
    result = 0
    for item in data:
        duplicates = [x for x in item if item.count(x) > 1]
        unique = [x for x in item if item.count(x) == 1]
        if len(unique) == 3:
            average_duplicates = sum(duplicates) / len(duplicates)
            average_unique = sum(unique) / len(unique)
            if average_unique < average_duplicates:
                result += 1
    print(result)
