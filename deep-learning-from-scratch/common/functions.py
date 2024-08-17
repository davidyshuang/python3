# coding: utf-8
""" 
Function printing python version.
"""

import numpy as np

def identity_function(x):
    """ identify function """
    return x


def step_function(x):
    """ Step function """
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    """ sigmoid function """
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    """ sigmoid grad  function """
    return (1.0 - sigmoid(x)) * sigmoid(x)

def relu(x):
    """ ReLU function """
    return np.maximum(0, x)


def relu_grad(x):
    """ ReLU grad function """
    grad = np.zeros(x)
    grad[x>=0] = 1
    return grad

def softmax(x):
    """ softmax function """
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    x = x - np.max(x) # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x))


def mean_squared_error(y, t):
    """ ReLU function """    
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    """ ReLU function """    
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size


def softmax_loss(x, t):
    """ ReLU function """    
    y = softmax(x)
    return cross_entropy_error(y, t)
