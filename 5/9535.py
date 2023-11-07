result = []
for N in range(1000):
    binary = bin(N)[2:]
    if N % 2 == 0:
        binary += "0"
    else:
        binary += "1"
    if binary.count("1") % 2 != 0:
        binary += "1"
    else:
        binary += "0"
    R = int(binary, 2)
    if R > 2023:
        result.append(R)
print(min(result))