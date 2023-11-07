result = []
for N in range(2, 1000):
    number = bin(N)[2:]
    if N % 3 == 0:
        number += number[-3:]
    else:
        number += bin((N % 3) * 3)[2:]
    R = int(number, 2)
    if R > 151:
        result.append(R)
print(min(result))