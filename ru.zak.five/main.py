import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def entropy(filename):
    """Функция вычисления энтропии по Шеннону.

    На вход подается список адресов файлов.
    На выходе получается список значений энтропии файлов.
    """
    entr_file = list()
    for i in filename:
        with open(i, 'rb') as f:
            a = np.array(list(f.read()))

        _, cnt = np.unique(a, return_counts=True)
        p = cnt / np.sum(cnt)
        H = -np.sum(p * np.log2(p))

        entr_file.append(H)

    return entr_file

Tk().withdraw()
filename = askopenfilenames()
entr = entropy(filename)

for i in range(len(filename)):
    print('Энтропия файла {}'.format(filename[i]), 'равна: {}'.format(entr[i]))

