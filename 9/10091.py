"""Откройте файл электронной таблицы, содержащей в каждой строке семь
натуральных чисел. Определите количество строк таблицы,
для чисел которых выполнены оба условия:
– в строке есть два числа, каждое из которых повторяется дважды, остальные
три числа различны;
– среднее арифметическое всех повторяющихся чисел строки меньше среднего
арифметического всех её чисел.
В ответе запишите только число."""
with open("10091") as file:
    data = [list(map(int, item.split())) for item in file]
    result = 0
    for item in data:
        duplicates = [x for x in item if item.count(x) > 1]
        if len(set(item)) == 5 and len(duplicates) == 4:
            sum_duplicates = sum(duplicates)
            count_duplicates = len(duplicates)
            if sum_duplicates / count_duplicates < sum(item) / len(item):
                result += 1
    print(result)
