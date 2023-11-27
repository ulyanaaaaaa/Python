import numpy as np

X=np.array([
        [1,2,61],
        [1,3,62],
        [1,4,73],
        [1,5,74],
        [1,6,80],
        [1,7,82],
        [1,8,69],
        [1,9,68],
        [1,10,81],
        [1,11,75],
        [1,12,71],
        [1,13,77]
])

Y=np.array([
        13.5,
        14.3,
        14.7,
        14.8,
        14.9,
        15.2,
        15.5,
        16.8,
        17.3,
        17.7,
        18.3,
        18.6
])

X_tr=X.T #транспонирование
X_tr_X=X_tr.dot(X)  #умножение
X_tr_X_revers=np.linalg.inv(X_tr_X) #обратная матрица
X_tr_Y=X_tr.dot(Y)
A=X_tr_X_revers.dot(X_tr_Y)
print("Вектор оценок А = ", A)

Y_end=X.dot(A)
print("Y = ", Y)
print("Y_end = ", Y_end)