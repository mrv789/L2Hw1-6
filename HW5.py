# аналогично, списал и не понял((

number = [9, 5, 7, 9, 9, 3, 3, 4, 5, 6, 9, 8]

rating = int(input('Введите элемент рейтинга: '))
inserted = False
for index, elem in enumerate(number):
    if rating > elem:
        number.insert(index, rating)
        inserted = True
        break

if not inserted:
    number.append(rating)

print(number)