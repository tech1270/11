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
        number = "1" + number + "02"
    else:
        number += converter((N % 3) * 4)
    R = int(number, 3)
    if R < 199:
        result.append(N)
print(max(result))