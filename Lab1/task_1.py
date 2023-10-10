numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

my_numbers = numbers[:4] + numbers[5:]

sum_of_numbers = sum(my_numbers)
count_of_numbers = len(numbers)
average_of_numbers = round(sum_of_numbers / count_of_numbers, 3)

numbers[4] = average_of_numbers
# TODO заменить значение пропущенного элемента средним арифметическим


print("Измененный список:", numbers)
