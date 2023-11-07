result = []
for N in range(1000):
    binary = bin(N)[2:]
    if N % 3 == 0:
        binary += binary[-3:]
    else:
        binary += bin((N % 3) * 3)[2:]
    R = int(binary, 2)
    if R > 151:
        result.append(R)
print(min(result))