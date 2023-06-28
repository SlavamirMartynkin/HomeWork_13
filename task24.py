# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
number = int(input('Введите количество кустов: '))
blueberries = []
for i in range(number):
    blueberries.append(random.randint(0, 10))
print(blueberries)

sum = 0
sum_list = []
for i in range(len(blueberries)):
    if i == 0:
        sum = blueberries[-1] + blueberries[i] + blueberries[i + 1]
        sum_list.append(sum)
        print(sum, end=' ')
    elif i == len(blueberries) - 1:
        sum = blueberries[i - 1] + blueberries[i] + blueberries[0]
        sum_list.append(sum)
        print(sum, end=' ')
    else:
        sum = blueberries[i - 1] + blueberries[i] + blueberries[i + 1]
        sum_list.append(sum)
        #print(sum, end=' ')
print(' ')
print(sum_list)
print(max(sum_list))