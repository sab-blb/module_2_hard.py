print(f"{"Задание"} {"«Слишком древний шифр»"}")

import random

def get_inset1():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = range(3, 21)
    inset1 = random.choice(numbers)
    return inset1

def get_password(n):
    password_dict = {}
    password_dict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645})
    password_dict.update({10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867})
    password_dict.update({14: 1611325212343114105968, 15: 1214114232133124115106978})
    password_dict.update({16: 1317115262143531341251161079, 17: 11621531441351261171089})
    password_dict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    password_dict.update({20: 13141911923282183731746416515614713812911})
    password = password_dict.get(n)
    return password

n = get_inset1()
print('Первая вставка:', n)

pair_number1 = range(1, n)
pair_number2 = range(1, n)
pairs = []
result = ''

for i in pair_number1:
    for j in pair_number2:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:
            multiples = n % (pn1 + pn2) #кратность
            if multiples == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print("Пары чисел второй вставки:", *pairs)
print("Пароль для второй вставки:", result)
if int(result) == get_password(n):
    print('Mission completed!', 'Выход из ловушки найден!')
