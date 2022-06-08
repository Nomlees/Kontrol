import random
import timeit
from matplotlib import pyplot as plt
import sort

sorting = sort.Sort()
variable = sort.Sort()
plt.figure(figsize=(12, 7))  # размер общего окна графиков
q = 1  # счетчик для последовательности окон графиков и их заголовков

for namesort in [sorting.bubble, sorting.insert, sorting.shell]:
    timerand, timeinc, timedec = variable.counting_time(namesort)

    plt.subplot(2, 2, q)
    plt.grid(True)
    plt.plot(timerand.keys(), timerand.values(), label='random')
    plt.plot(timeinc.keys(), timeinc.values(), label='increase')
    plt.plot(timedec.keys(), timedec.values(), label='decrease')
    listtitlesort = [' ', 'Сортировка пузырьком', 'Сортировка вставками', 'Сортировка Шелла']
    titlesort = listtitlesort[q]
    plt.title('{}'.format(titlesort))
    plt.ylabel('секунды')
    plt.legend()
    q += 1

plt.show()
