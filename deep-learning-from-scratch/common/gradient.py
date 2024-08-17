# coding: utf-8
""" Module Description """
import numpy as np

def _numerical_gradient_1d(f, x):
    """ function description """
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        x[idx] = tmp_val - h
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 値を元に戻す
    return grad


def numerical_gradient_2d(f, y):
    """ ReLU function """
    if y.ndim == 1:
        return _numerical_gradient_1d(f, y)
    else:
        grad = np.zeros_like(y)
        for idx, x in enumerate(y):
            grad[idx] = _numerical_gradient_1d(f, x)
        return grad


def numerical_gradient(f, x):
    """ ReLU function """
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        x[idx] = tmp_val - h
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val # 値を元に戻す
        it.iternext()

    return grad
