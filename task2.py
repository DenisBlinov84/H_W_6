# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
# значение с доверительной вероятностью 0,95.

import scipy.stats as stats
import numpy as np

a = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])

n = len(a)  # объём выборки

X = np.mean(a)  # Выборочное среднее

S = np.std(a, ddof=1)  # сигма не смещённая

t = stats.t.ppf(0.975, 9)

L = X-t*S/np.sqrt(n)  # нижняя граница интервала
U = X+t*S/np.sqrt(n)  # верхняя граница интервала

print('Ответ: ', '[', L, ';', U, ']')

