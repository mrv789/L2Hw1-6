
# пришлось списать, т.к. вообще не понял суть задачи и его решение)))

user_numbers = input('Введите числа:')

# print(user_numbers)

input_numbers = user_numbers.split()

# print(input_numbers)
# print(type(input_numbers))

len_list = len(input_numbers)
i = 0
if len_list > 1:
    while i < len_list - 1:
        input_numbers[i], input_numbers[i+1] = input_numbers[i+1], input_numbers[i]
        i += 2
print(input_numbers)
