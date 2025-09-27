#неявная

import numpy as np

time = 8 # время
H = 0.1
t0 = 550 #левая граница пластины
th = 700 #правая граница пластины 
t_start = 350 #остальная пластина в начале
ro = 8800 # плотность
c = 381 # теплоёмкость
lam = 384 # теплопроводность лямбда
m = 100 #разбиение по времени
n = 100 #разбиение по координате, точки нумернуются от 1 до n, количество разбиений n - 1

h = H / (n - 1)
tau = time / m

alpha = np.zeros((n))
beta = np.zeros((n))
alpha[0] = 0
beta[0] = t0
A = lam / h ** 2
B = 2 * lam / h ** 2 + ro * c / tau
C = lam / h ** 2
def D(T):
    d = - ro * c * T / tau
    return d

# к и к+1 - моменты времени, i - координаты

t = np.zeros((m, n)) #по строкам время, по столбцам координаты

t[:, 0] = t0
t[:, n - 1] = th
t[:, 1 : n - 1] = t_start
t_new = np.copy(t)
#print(t)

for k in range(m - 1):
    for i in range(1, n - 1):
        beta[i] = np.copy((C * beta[i - 1] - D(t_new[k, i])) / (B - C * alpha[i - 1]))
        alpha[i] = np.copy(A / (B - C * alpha[i - 1]))
    for i in range(n - 1, 0, -1):
        t_new[k + 1, i - 1] = np.copy(alpha[i - 1] * t_new[k + 1, i] + beta[i - 1])
      

with np.printoptions(precision=0, threshold=np.inf):
    print(t_new)
