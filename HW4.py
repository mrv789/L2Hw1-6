# Вообще не понятно как и почему именно так(((


user_input = input('Введите любые слова: ')

words = user_input.split()
for num, word in enumerate (words):
    print(f'#{num} - {word[:10]}')