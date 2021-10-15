user_mounth = input('Введите числовой номер месяца года: ')

s1 = 'Зима'
s2 = 'Весна'
s3 = 'Лето'
s4 = 'Осень'

month_list = {'1' : s1, '2' : s1, '3' : s2, '4' : s2, '5' : s2, '6' : s3, '7' : s3, '8' : s3, '9' : s4, '10' : s4, '11' : s4, '12' : s1}

print(month_list[user_mounth])

season_list = [s1, s1, s2, s2, s2, s3, s3, s3, s4, s4, s4, s1]

# зачем тогда это?
# print(month_list[int(user_mounth) - 1])
