def converter(number):
    result = ""
    while number:
        result = str(number % 6) + result
        number //= 6
    return result

result = []
for N in range(1, 1000):
    number = converter(N)
    if N % 3 == 0:
        number += number[:2]
    else:
        number += converter((N % 3) * 10)
    R = int(number, 6)
    if R > 680:
        result.append(R)
print(min(result))
