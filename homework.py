# ------- д/з
{

}

# ------- д/з 14.1
{
    # def prn_list(x, new_row = False):
    #     if len(x) == 0:
    #         print('Конец списка')
    #         return
    #
    #     if new_row:
    #         c_end = '\n'
    #     else:
    #         c_end = ''
    #
    #     print(f'{x[0]}  ', end=c_end)
    #     prn_list(x[1:], new_row)
    #
    #
    # arrX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    #
    # prn_list(arrX)
    # prn_list(arrX, True)
}

# ------- д/з 13.1
{
    # import random
    #
    #
    # def matrix_init(x=2, y=2, val_from=-100, val_to=100):
    #     return [[random.randint(val_from, val_to) for j in range(x)] for i in range(y)]
    #
    #
    # def matrix_add(m_a, m_b):
    #     return [[m_a[i][j] + m_b[i][j] for j in range (len(m_a[0]))] for i in range(len(m_a))]
    #
    #
    # def pl(t):
    #     for i in t:
    #         print(*i)
    #
    #
    # # параметры генерации матриц
    # valX = random.randint(1, 10)
    # valY = random.randint(1, 10)
    # valFrom = -random.randint(1, 200)
    # valTo = random.randint(1, 200)
    #
    # m1 = matrix_init(valX, valY, valFrom, valTo)
    # m2 = matrix_init(valX, valY, valFrom, valTo)
    # m3 = matrix_add(m1, m2)
    #
    # pl(m1)
    # print()
    # pl(m2)
    # print()
    # pl(m3)
}

# ------- д/з 11.2
{
    # import collections
    #
    #
    # def name_field(field_id):
    #     if field_id == 1:
    #         return 'ID'
    #     elif field_id == 2:
    #         return 'Name'
    #     elif field_id == 3:
    #         return 'Вид питомца'
    #     elif field_id == 4:
    #         return 'Возраст питомца'
    #     elif field_id == 5:
    #         return 'Имя владельца'
    #     else:
    #         return 'noname'
    #
    #
    # def pet_item():
    # # контроль корректировки старой информации намеренно опущен
    # # потому что считаю бессмысленным такое "расширение" программы в рамках данной темы
    #     pet_cur = dict()
    #     pet_param = dict()
    #
    #     pet_name = str(input('Введите кличку питомца '))
    #     pet_type = str(input('   ' + name_field(3) + ' '))
    #     pet_age = int(input('   ' + name_field(4) + ' '))
    #     pet_owner = str(input('   ' + name_field(5) + ' '))
    #
    #     pet_param[name_field(3)] = pet_type
    #     pet_param[name_field(4)] = pet_age
    #     pet_param[name_field(5)] = pet_owner
    #
    #     pet_cur[pet_name] = pet_param
    #     return pet_cur
    #
    #
    # def create():
    #     last = collections.deque(pets, maxlen=1)[0]
    #     last += 1
    #
    #     pets[last] = pet_item()
    #
    #     print()
    #     print(f'Добавлен новый питомец:')
    #     read(last)
    #
    #     return True
    #
    #
    # def read(pet_id):
    #     dict_pet = get_pet(pet_id)
    #     if not dict_pet:
    #         print('Такого питомца в БД нет!')
    #         return
    #
    #     print(f'({pet_id}) ', end='')
    #     print(f'Это {dict_pet[name_field(3)]} по кличке "{dict_pet[name_field(2)]}". ', end='')
    #     print(f'{name_field(4)}: {dict_pet[name_field(4)]} {get_suffix(dict_pet[name_field(4)])}. ', end='')
    #     print(f'{name_field(5)}: {dict_pet[name_field(5)]}.')
    #
    #
    # def update(pet_id):
    #     dict_pet = get_pet(pet_id)
    #     if not dict_pet:
    #         print('Такого питомца в БД нет!')
    #         return
    #
    #     print()
    #     pets[pet_id] = pet_item()
    #     print(f'Обновлена информация по питомцу {pet_id}:')
    #     return
    #
    #
    # def delete(pet_id):
    #     dict_pet = get_pet(pet_id)
    #     if not dict_pet:
    #         print('Такого питомца в БД нет!')
    #         return
    #
    #     pets.__delitem__(pet_id)
    #     print(f'Удалена информация по питомцу {pet_id}:')
    #     return
    #
    #
    # def get_pet(pet_id):
    #     dict_pet = {}
    #
    #     for petID, petData in pets.items():
    #         if petID == pet_id:
    #             dict_pet[name_field(1)] = petID
    #             for keyPet in petData.keys():
    #                 dict_pet[name_field(2)] = keyPet
    #             for petName, petParam in petData.items():
    #                 dict_pet[name_field(3)] = petParam[name_field(3)]
    #                 dict_pet[name_field(4)] = petParam[name_field(4)]
    #                 dict_pet[name_field(5)] = petParam[name_field(5)]
    #             return dict_pet
    #
    #     return False
    #
    #
    # def get_suffix(age):
    #     # расписываем возраст
    #     age100 = age % 100
    #     age10 = age % 10
    #     if (age100 > 10) and (age100 < 20):
    #         return 'лет'
    #     else:
    #         if age10 == 1:
    #             return 'год'
    #         elif (age10 > 1) and (age10 < 5):
    #             return 'года'
    #     return 'лет'
    #
    #
    # def pets_list():
    #     for petID in pets.keys():
    #         read(petID)
    #
    #
    # pets = {
    #     1:
    #         {
    #             'Каа': {
    #                 'Вид питомца': 'желторотый питон',
    #                 'Возраст питомца': 12,
    #                 'Имя владельца': 'Саша',
    #             },
    #         },
    #     2:
    #         {
    #             'Багира': {
    #                 'Вид питомца': 'мейнкун',
    #                 'Возраст питомца': 3,
    #                 'Имя владельца': 'Ира',
    #             },
    #         },
    #     3:
    #         {
    #             'Лаки': {
    #                 'Вид питомца': 'хаск',
    #                 'Возраст питомца': 12,
    #                 'Имя владельца': 'Стас',
    #             },
    #         },
    #     4:
    #         {
    #             'Мухтар': {
    #                 'Вид питомца': 'собака',
    #                 'Возраст питомца': 9,
    #                 'Имя владельца': 'Маша',
    #             },
    #         }
    # }
    #
    # cmdCur = ''
    #
    # while cmdCur.upper() not in ['STOP', 'EXIT', 'QUIT', 'ESC']:
    #     if cmdCur.upper() == 'LIST':
    #         print()
    #         pets_list()
    #
    #     elif cmdCur.upper() == 'READ':
    #         read(int(input('Введите ID питомца: ')))
    #
    #     elif cmdCur.upper() == 'CREATE':
    #         create()
    #
    #     elif cmdCur.upper() == 'UPDATE':
    #         update(int(input('Введите ID питомца: ')))
    #
    #     elif cmdCur.upper() == 'DELETE':
    #         delete(int(input('Введите ID питомца: ')))
    #
    #     elif cmdCur == '':
    #         cmdCur = 'continue'
    #
    #     else:
    #         print('Нераспознанная команда.')
    #         print()
    #         print('Список используемых команд:')
    #         print('CREATE              - добавить нового питомца')
    #         print('READ                - информация о питомце')
    #         print('UPDATE              - редактировать данные по питомцу')
    #         print('DELETE              - удалить данные по питомцу')
    #         print('LIST                - вывести список всех питомцев')
    #         print('STOP/QUIT/EXIT/ESC  - завершить работу')
    #
    #     print()
    #     cmdCur = str(input('введите команду: '))
}

# ------- д/з 11.1
{
    # import random
    #
    #
    # def factorial(x):
    #     if x == 1:
    #         return 1
    #     return x * factorial(x-1)
    #
    # nHow = random.randint(1, 4)
    # arrNum = []
    #
    # print()
    # print(f'Выбрано число {nHow}')
    # nHow = factorial(nHow)
    # print(f'Факториал = {nHow}')
    #
    # for i in range(nHow, 0, -1):
    #     arrNum.append(factorial(i))
    #
    # # print(factorial(6))
    # print(f'Список факториалов от {nHow} до 1')
    # print(arrNum)
}

# ------- д/з 10.2
{
    # dictNum = {}
    #
    # for i in range(10, -6, -1):
    #     dictNum[i] = i ** i
    #     print(f'{i}: {dictNum[i]}')
    #
    # print(dictNum)
}

# ------- д/з 10.1
{
    # howPet = 1
    # pets = {}
    # strPetType = 'Вид питомца'
    # strPetAge = 'Возраст питомца'
    # strPetOwner = 'Имя владельца'
    #
    # while howPet != 0:
    #     petCur = dict()
    #     petParam = dict()
    # # новый питомец
    #     namePet = str(input('Введите имя питомца '))
    # # --- тип, возраст, владелец
    #     petType = str(input('   ' + strPetType + ' '))
    #     petAge = int(input('   ' + strPetAge + ' '))
    #     petOwner = str(input('   ' + strPetOwner + ' '))
    #
    #     petParam[strPetType] = petType
    #     petParam[strPetAge] = petAge
    #     petParam[strPetOwner] = petOwner
    #
    #     petCur[namePet] = petParam
    #
    # # добавляем питомца в словарь
    #     pets.update(petCur)
    #     howPet = int(input('продолжаем ? (0/1) '))
    #
    # print()
    # # print(pets)
    # for petName in pets.keys():
    #     print(f'Это {pets[petName][strPetType]} по кличке "{petName}". ', end='')
    #
    # # расписываем возраст
    #     nAge10 = pets[petName][strPetAge] % 100
    #     nAge = pets[petName][strPetAge] % 10
    #     if (nAge10 > 10) and (nAge10 < 20):
    #         strAge = 'лет'
    #     else:
    #         if nAge == 1:
    #             strAge = 'год'
    #         elif (nAge > 1) and (nAge < 5):
    #             strAge = 'года'
    #         else:
    #             strAge = 'лет'
    #
    #     print(f'{strPetAge}: {pets[petName][strPetAge]} {strAge}. ', end='')
    #     print(f'{strPetOwner}: {pets[petName][strPetOwner]}.')
}

# ------- д/з 9.3
{
    # import random
    #
    # # ------- БЛОК РУЧНОГО ФОРМИРОВАНИЯ ТЕСТОВОГО НАБОРА
    # # arrNum1 = map(int, input('Введите наборцелых значений ').split())
    #
    # # ------- БЛОК АВТОМАТИЧЕСКОГО ФОРМИРОВАНИЯ ТЕСТОВОГО НАБОРА
    # nHow = random.randint(1, 10 ** 2)
    # print('Введите кол-во чисел: ', nHow)
    # arrNum1 = []
    # nLim = 10 ** 2          #рабочий диапазон случайных чисел
    #
    # for i in range(nHow):
    #     arrNum1.append(random.randint(1, nLim))
    #
    # # ------- ОСНОВНОЙ БЛОК
    # setNum1 = set()
    #
    # print()
    # for i in arrNum1:
    #     if i in setNum1:
    #         print(f'{i} - YES')
    #     else:
    #         print(f'{i} - NO')
    #         setNum1.add(i)
    #
    # print()
    # print('исходный набор случайных чисел (кол-во):', len(arrNum1))
    # print('множество (кол-во)                     :', len(setNum1))
}

# ------- д/з 9.2
{
    # import random
    #
    # # nHow = random.randint(1, 10 ** 5)
    # nHow = random.randint(1, 10 ** 4)
    # print('Введите кол-во чисел: ', nHow)
    # arrNum1 = []
    # arrNum2 = []
    # # nLim = 2 * 10 ** 9    #исходный диапазон
    # nLim = 10 ** 6          #рабочий диапазон. исходный уменьшен для большей результативности
    #
    # for i in range(nHow):
    #     arrNum1.append(random.randint(-nLim, nLim))
    #     arrNum2.append(random.randint(-nLim, nLim))
    #
    # setNum1 = set(arrNum1)
    # setNum2 = set(arrNum2)
    #
    # print()
    # print('1-й исходный набор случайных чисел (кол-во):', len(arrNum1))
    # print('2-й исходный набор случайных чисел (кол-во):', len(arrNum2))
    # print('1-е множество (кол-во)                     :', len(setNum1))
    # print('2-е множество (кол-во)                     :', len(setNum2))
    # print('Содержатся и в 1-м и во 2-м (кол-во)       :', len(setNum1.intersection(setNum2)))
    # print('Содержатся и в 1-м и во 2-м                :', setNum1.intersection(setNum2))
}

# ------- д/з 9.1
{
    # import random
    #
    # nHow = random.randint(1, 10 ** 5)
    # print('Введите кол-во чисел: ', nHow)
    # aNum = []
    # # nLim = 2 * 10 ** 9    #исходный диапазон
    # nLim = 10 ** 6          #рабочий диапазон. исходный уменьшен для большей результативности
    #
    # for i in range(nHow):
    #     aNum.append(random.randint(-nLim, nLim))
    #
    # setNum = set(aNum)
    #
    # print()
    # print('Исходный набор случайных чисел (кол-во):', len(aNum))
    # print('Из них уникальных (кол-во)             :', len(setNum))
}

# ------- д/з 8.3
{
    # import random
    #
    # nHow = random.randint(1, 100)
    # weightMax = random.randint(1, 10 ** 6)
    # print('Введите кол-во рыбаков и максимальную грузоподъёмность лодки: ', nHow, weightMax)
    # aWeight = []
    # cntBot = 1
    #
    # for i in range(nHow):
    #     aWeight.append(random.randint(1, weightMax))
    #
    # print()
    # print(f'Минимальное кол-во необходимых лодок - {cntBot}')
}

# ------- д/з 8.2
{
    # import random
    #
    # nHow = int(input('Введите кол-во '))
    # aTest = []
    # aRes = []
    #
    # for i in range(nHow):
    #     aTest.append(random.randint(1, 10000))
    # print('Введите значения', *aTest)
    #
    # aRes.append(aTest[-1])
    # for i in range(len(aTest) - 1):
    #     aRes.append(aTest[i])
    #
    # print()
    # print('Исходный массив', aTest)
    # print('Конечный массив', aRes)
}

# ------- д/з 8.1
{
    # import random
    #
    # nHow = int(input('Введите кол-во '))
    # aTest = []
    # for i in range(nHow):
    #     aTest.append(random.randint(-10000, 10000))
    #
    # aTestR = aTest[::-1]
    #
    # print()
    # print(aTest)
    # print(aTestR)
}

# ------- д/з 7.2
{
    # #А    роза    упала    на    лапу    Азора
    # checkStr = str(input('Введите строку '))
    # str1 = checkStr.replace('  ', ' ')
    #
    # nLen = -1
    # while nLen != len(str1):
    #     nLen = len(str1)
    #     str1 = str1.replace('  ', ' ')
    #
    # print()
    # print(checkStr)
    # print(str1)
}

# ------- д/з 7.1
{
    # #А роза упала на лапу Азора
    # #Was it a car or a cat I saw
    # checkStr = str(input('Введите строку '))
    # str1 = checkStr.replace(' ', '').upper()
    # # str2 = str1[::-1]
    #
    # # if str1 == str2:
    # print()
    # if str1 == str1[::-1]:
    #     print(f'Строка "{checkStr}" - палиндром')
    # else:
    #     print(f'Строка "{checkStr}" - НЕ палиндром')
}

# ------- д/з 6.3
{
    # valA = 0
    # valB = -1
    #
    # while valA > valB:
    #     valA, valB = map(int, input('Введите диапазон A...B ').split())
    #
    #     # вариант ДО ЛЕКЦИИ 7."СТРОКИ"
    # strRes = ''
    # for valCur in range(valA, valB + 1):
    #     if valCur % 2 == 0:
    #         strRes += str(valCur) + ' '
    #
    # print()
    # print('Чётные числа в заданном диапазоне:', strRes)
    #
    # # вариант ПОСЛЕ ЛЕКЦИИ 7."СТРОКИ"
    # print()
    # print('Чётные числа в заданном диапазоне: ', end='')
    # for valCur in range(valA, valB + 1):
    #     if valCur % 2 == 0:
    #         print(f'{valCur} ', end='')
}

# ------- д/з 6.2
{
    # valNat = 0
    # while valNat not in range(1, 2 * 10 ** 9 + 1):
    #     valNat = int(input('Введите число от 1 до 2 000 000 000 '))
    #
    # divNum = 2
    # valCur = 1
    #
    # # вариант for
    # # for valCur in range(2, int(valNat / 2) + 1):
    #
    # # вариант while
    # while valCur <= int(valNat / 2):
    #     valCur += 1
    #
    #     if valNat % valCur == 0:
    #         divNum += 1
    #
    # print()
    # print(f'Кол-во делителей числа {valNat} - {divNum}.')
    # if divNum == 2:
    #     print(f'Число {valNat} - простое')
}

# ------- д/з 5.2
{
    # inpWord = input('Введите слово на латинице ')
    #
    # cntA = inpWord.count('a')
    # cntE = inpWord.count('e')
    # cntI = inpWord.count('i')
    # cntO = inpWord.count('o')
    # cntU = inpWord.count('u')
    #
    # cntWord = len(inpWord)
    # cntVowels = cntA + cntE + cntI + cntO + cntU
    # cntConsonants = cntWord - cntVowels
    #
    # print()
    # print(f"В слове '{inpWord}', гласных букв: {cntVowels}, согласных букв: {cntConsonants}")
    #
    # print(f"Букв 'a' в слове {inpWord}: {cntA}" if cntA > 0 else False)
    # print(f"Букв 'e' в слове {inpWord}: {cntE}" if cntE > 0 else False)
    # print(f"Букв 'i' в слове {inpWord}: {cntI}" if cntI > 0 else False)
    # print(f"Букв 'o' в слове {inpWord}: {cntO}" if cntO > 0 else False)
    # print(f"Букв 'u' в слове {inpWord}: {cntU}" if cntU > 0 else False)
}

# ------- д/з 6.1
{
    # nHow = int(input('Сколько? '))
    # cnt = 0
    # for i in range(nHow):
    #     nCur = int(input(str(i+1) + ' ? '))
    #     if nCur == 0:
    #         cnt += 1
    #
    # print()
    # print('Было', cnt, 'нулевых значений')
}

# ------- д/з 5.3
{
    # # sumMin = float(input('Минимальная сумма инвестиций '))
    # # sumMike = float(input('Сумма инвестиций Майкла '))
    # # sumIvan = float(input('Сумма инвестиций Ивана '))
    # sumMin, sumMike, sumIvan = map(float, input('Суммы (мин, М, И) ').split())
    #
    # print()
    # if (sumMike >= sumMin) and (sumIvan >= sumMin)    :
    #     print(2)
    # elif sumMike >= sumMin:
    #     print('Mike')
    # elif sumIvan >= sumMin:
    #     print('Ivan')
    # elif (sumMike + sumIvan) >= sumMin:
    #     print(1)
    # else:
    #     print(0)
}

# ------- д/з 5.1
{
    # x = int(input('Введите целое число '))
    #
    # if x % 2 == 1:
    #     sType = 'нечётное'
    # else:
    #     sType = 'чётное'
    #
    # if x > 0:
    #     sSign = 'положительное'
    # elif x < 0:
    #     sSign = 'отрицательное'
    # else:
    #     sType = ''
    #     sSign = 'нулевое'
    #
    # print('Введено', sSign, sType, 'число')
    # if x % 2 == 1:
    #     print('число не является чётным')
}

# ------- д/з 4.2
{
    # a = int(input('Ввежите пятизначное целое число '))
    #
    # a1 = a // 10000
    # a2 = (a % 10000) // 1000
    # a3 = (a % 1000) // 100
    # a4 = (a % 100) // 10
    # a5 = (a % 10)
    # aRes = a4 ** a5 * a3 / (a1 - a2)
    #
    # print()
    # print(a, a1, a2, a3, a4, a5, aRes, sep=' --> ')
}

# ------- д/з 4.1
{
    # a, b = map(float, input('Через пробел введите длину и ширину прямоугольника ').split())
    #
    # print()
    # print('S -', a * b)
    # print('P -', (a * b) * 2)
}

# ------- д/з 3.2
{
    # #https://itest.kz/ru/ent/biologiya/11-klass/lecture/osnovnye-etapy-evolyucii-cheloveka
    # #дриопитек – рамапитек – австралопитек – человек умелый – человек прямоходящий – палеоантроп – неоантроп
    #
    # print('Введите этапы развития человека')
    # stage1 = input('1-й ')
    # stage2 = input('2-й ')
    # stage3 = input('3-й ')
    # stage4 = input('4-й ')
    # stage5 = input('5-й ')
    # stage6 = input('6-й ')
    # stage7 = input('7-й ')
    #
    # print()
    # print(stage1, stage2, stage3, stage4, stage5, stage6, stage7, sep=' => ')
}

# ------- д/з 3.1
{
    # petType = input("Введите вид питомца ")
    # petName = input("Кличка питомца? ")
    # petAge = input("Возраст питомца? ")
    #
    # print()
    # print('Это', petType, 'по кличке', '"' + petName + '".', 'Возраст:', petAge, 'года.')
}
