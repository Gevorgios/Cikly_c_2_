# start = int(input("Введите начальное число диапазона: "))
# end = int(input("Введите конечное число диапазона: "))
#
# sum_even = 0
# sum_odd = 0
# sum_divisible_by_9 = 0
# count_even = 0
# count_odd = 0
# count_divisible_by_9 = 0
#
# for num in range(start, end+1):
#     if num % 2 == 0:
#         sum_even += num
#         count_even += 1
#     else:
#         sum_odd += num
#         count_odd += 1
#     if num % 9 == 0:
#         sum_divisible_by_9 += num
#         count_divisible_by_9 += 1
#
# average_even = sum_even / count_even
# average_odd = sum_odd / count_odd
# average_divisible_by_9 = sum_divisible_by_9 / count_divisible_by_9
#
# print("Сумма четных чисел:", sum_even)
# print("Сумма нечетных чисел:", sum_odd)
# print("Сумма чисел, кратных 9:", sum_divisible_by_9)
#
# print("Среднеарифметическое четных чисел:", average_even)
# print("Среднеарифметическое нечетных чисел:", average_odd)
# print("Среднеарифметическое чисел, кратных 9:", average_divisible_by_9)

# length = int(input("Введите длину линии: "))
# symbol = input("Введите символ для заполнения линии: ")
#
# for i in range(length):
#     print(symbol)

# while True:
#     number = int(input("Введите число: "))
#
#     if number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     else:
#         print("Number is equal to zero")
#
#     if number == 7:
#         print("Good bye!")
#         break

# numbers = []
# while True:
#     number = int(input("Введите число: "))
#
#     numbers.append(number)  # Добавляем введенное число в список
#
#     if number == 7:
#         print("Good bye!")
#         break
#
# sum_numbers = sum(numbers)  # Суммируем все введенные числа
# max_number = max(numbers)  # Находим максимальное число
# min_number = min(numbers)  # Находим минимальное число
#
# print(f"Сумма чисел: {sum_numbers}")
# print(f"Максимальное число: {max_number}")
# print(f"Минимальное число: {min_number}")
