number = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 \
         ** 4 - 2024
result = ""
while number:
    result += str(number % 25)
    number //= 25
print(result.count("0"))
