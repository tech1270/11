def converter(number):
    result = ""
    while number:
        result = str(number % 3) + result
        number //= 3
    return result


result = []
for N in range(11, 1000):
    number = converter(N)
    even = [x for x in number if int(x) % 2 == 0]
    odd = [x for x in number if int(x) % 2 != 0]
    if len(even) > len(odd):
        number = "22" + number
    else:
        number = "11" + number
    R = int(number, 3)
    if R > 100:
        result.append(R)
print(min(result))