numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


missing_number_index = numbers.index(None)
my_numbers = numbers[:missing_number_index] + numbers[missing_number_index + 1:]

sum_of_numbers = sum(my_numbers)
count_of_numbers = len(numbers)
average_of_numbers = round(sum_of_numbers / count_of_numbers, 3)

numbers[missing_number_index] = average_of_numbers
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
