# Императивное: Найти сумму всех четных чисел в списке

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = 0

for num in numbers:
    if num % 2 == 0:
        sum_of_even += num

print("Сумма четных чисел (императивно):", sum_of_even)


# Декларативное: Найти сумму всех четных чисел в списке

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = sum(filter(lambda x: x % 2 == 0, numbers))

print("Сумма четных чисел (декларативно):", sum_of_even)


# Императивное: Найти сумму всех чисел в списке, больших 5

numbers = [1, 6, 3, 8, 5, 10, 7]
sum_above_5 = 0

for num in numbers:
    if num > 5:
        sum_above_5 += num

print("Сумма чисел больших 5 (императивно):", sum_above_5)


# Декларативное: Найти сумму всех чисел в списке, больших 5

numbers = [1, 6, 3, 8, 5, 10, 7]
sum_above_5 = sum(filter(lambda x: x > 5, numbers))

print("Сумма чисел больших 5 (декларативно):", sum_above_5)