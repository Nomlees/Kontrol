from scipy import integrate
import matplotlib.pyplot as plt
import meth as mod
import math
meth_calc_int = mod.Methods() # meth_calc_int объект класса Methods

def function(x):
    """Исходная функция"""
    return math.cos(6 * math.pow(2, 2) + 2 * x - 2 * math.pow(x, 2))



val_b = [-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #значения верхнего предела
                                                                                                  #нижний передел фиксированный а = -1
NL = dict()
for b in val_b: # истинные значения
    NL[b] = integrate.quad(function, -1, b)[0]

plt.figure(figsize=(12, 7))
q = 1
for i in [1, 5, 10, 100]: # количество проходов
    plt.subplot(2, 2, q)
    plt.grid(True)
    q += 1
    plt.plot(NL.keys(), NL.values(), label = 'true')
    plt.plot(meth_calc_int.sympson(function, i, val_b).keys(), meth_calc_int.sympson(function, i, val_b).values(), label = 'sympson')
    plt.plot(meth_calc_int.rect(function, i, val_b).keys(), meth_calc_int.rect(function, i, val_b).values(), label = 'rect')
    plt.plot(meth_calc_int.trap(function, i, val_b).keys(), meth_calc_int.trap(function, i, val_b).values(), label = 'trap')
    plt.title('Количество проходов {}'.format(i), fontsize = 10)
    plt.legend()

plt.show()
