import numpy as np
import csv
from sklearn import preprocessing

from collections import defaultdict

np.seterr(all='ignore')


def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))


float_formatter = lambda x: "%.3f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})
X = np.genfromtxt('DelayedFlights.csv', delimiter=",", usecols=( 12, 13, 14), skip_header=1, max_rows=100)
y = np.genfromtxt('DelayedFlights.csv', delimiter=",", usecols=(15, 16), skip_header=1, max_rows=100)
X = X[~np.isnan(X).any(axis=1)]
y = y[~np.isnan(y).any(axis=1)]
X = preprocessing.normalize(X)
y = preprocessing.normalize(y)

np.random.shuffle(X)
np.random.shuffle(y)

# print(X[0])
# print(y[0])
np.random.seed(1)

syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 8)) - 1
syn2 = 2 * np.random.random((8, 32)) - 1
syn3 = 2 * np.random.random((32, 16)) - 1
syn4 = 2 * np.random.random((16, 4)) - 1
syn5 = 2 * np.random.random((4, 2)) - 1

for j in range(10001):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))
    l4 = nonlin(np.dot(l3, syn3))
    l5 = nonlin(np.dot(l4, syn4))
    l6 = nonlin(np.dot(l5, syn5))


    # how much did we miss the target value?
    l6_error = y - l6
    print("iteration " + str(j))
    if (j % 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l6_error))))

    l6_delta = l6_error * nonlin(l6, deriv=True)
    l5_error = l6_delta.dot(syn5.T)
    l5_delta = l5_error * nonlin(l5, deriv=True)
    l4_error = l5_delta.dot(syn4.T)
    l4_delta = l4_error * nonlin(l4, deriv=True)
    l3_error = l4_delta.dot(syn3.T)
    l3_delta = l3_error * nonlin(l3, deriv=True)
    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn5 += l5.T.dot(l6_delta)
    syn4 += l4.T.dot(l5_delta)
    syn3 += l3.T.dot(l4_delta)
    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

# print("Synapse 3")
# print(syn3)
# print("Synapse 2")
# print(syn2)
# print("Synapse 1")
# print(syn1)
# print("Synapse 0")
# print(syn0)
# print(l4)
print("test")
X = X[0]
print(X)
print(y[0])
l0 = X
l1 = nonlin(np.dot(l0, syn0))
l2 = nonlin(np.dot(l1, syn1))
l3 = nonlin(np.dot(l2, syn2))
l4 = nonlin(np.dot(l3, syn3))
l5 = nonlin(np.dot(l4, syn4))
l6 = nonlin(np.dot(l5, syn5))
print(l6)
