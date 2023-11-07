result = []
for N in range(10000):
    number = bin(N)[2:]
    summ = number.count("1")
    if N % 2 == 0:
        if summ % 2 == 0:
            bit = "0"
        else:
            bit = "1"
        number = bin(summ)[2:] + number + bit
    else:
        number += "0" + bin(summ)[2:]
    R = int(number, 2)
    if R < 256:
        result.append((R, N))
print(max(result)[1]
