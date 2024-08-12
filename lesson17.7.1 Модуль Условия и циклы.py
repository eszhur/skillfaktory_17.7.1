multipl = 1
for number in range(1, 11):
    if number % 2 == 0:
        continue
    multipl *= number

print("Произведение всех нечетных чисел от 1 до 10:", multipl)

