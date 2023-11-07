
def converter(number):
    result = ""
    while number:
        result += str(number % 3)
        number //= 3
    return result[::-1]


result = []
for N in range(2, 1000):
    number = converter(N)
    summ = sum(map(int, number))
    if summ % 3 == 0:
        number = "20" + number
    else:
        number = "10" + number
    R = int(number, 3)
    if R <= 100:
        result.append(N)
print(max(result))