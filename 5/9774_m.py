def converter(number):
    result = ""
    while number:
        result = str(number % 3) + result
        number //= 3
    return result

result = []
for N in range(1, 1000):
    number = converter(N)
    if N % 3 == 0:
        number += number[-2:]
    else:
        number += converter((N % 3) * 5)
    R = int(number, 3)
    if R > 133:
        result.append(R)
print(min(result))