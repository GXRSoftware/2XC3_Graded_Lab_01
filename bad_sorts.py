"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

# Optimized Bubble sort
def bubble_sort2(L):  # LOOK HERE
    for i in range(len(L)):
        swaped = False
        for j in range(len(L) - i - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                swaped = True
        if not swaped:
            break
# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)

def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def selection_sort2(L):
    i = 0
    l = len(L) - 1
    while i < l:
        min_index, max_index = find_indexes(L, i, l)  #LOOK HERE
        if (i == max_index):           #LOOK HERE
            swap(L, i, min_index)
        else:
            swap(L, i, min_index)
            swap(L, l, max_index)      #LOOK HERE
        i += 1
        l -= 1

def find_indexes(L, n, e):
    min_index = n
    max_index = n                  #LOOK HERE
    for i in range(n+1, e + 1):
        if L[i] < L[min_index]:
            min_index = i
        if L[i] > L[max_index]:    #LOOK HERE
            max_index = i
    return min_index, max_index


import matplotlib
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
import math
from graph_algo import graph # imported from experiment 1

if __name__ == "__main__":
    ###############################################################
    #                      Experiment 1:                          #
    ###############################################################
    expertiment1_test_datas = [ 
        create_random_list(10, 10), # a list of 10 elements in range 0 ... 10
        create_random_list(100, 70), # a list of 20 elements in range 0 ... 70
        create_random_list(1000, 100), # a list of 50 elements in range 0 ... 100
        create_random_list(1500, 500), # a list of 70 elements in range 0 ... 100
        create_random_list(2000, 1000), # a list of 100 elements in range 0 ... 100
    ]

    graph(selection_sort, insertion_sort, bubble_sort, filePath="./Graphs/experiment1.png",
          title = 'Runtime Comparison of Insertion, Selection, and Bubble sorts', 
          colors = ("r", "b", "g"), datas= expertiment1_test_datas
    )

    #######
    #  2  #
    #######
    lengths = [2**x for x in range(13)]
    max_value = 2**30
    lists = [create_random_list(_, max_value) for _ in lengths]

    n = len(lengths)
    total1, total2, total3 = 0, 0, 0
    data1, data2, data3 = [], [], []
    cmp1, cmp2, cmp3 = [], [], []
    value = random.randint(0, max_value)

    for _ in range(n):
        print(_)
        L = lists[_]
        L1 = [*L]
        L2 = [*L]

        start = timeit.default_timer()
        bubble_sort(L1)
        elapsed = timeit.default_timer() - start
        total1 += elapsed
        data1.append(elapsed)

        start = timeit.default_timer()
        bubble_sort2(L2)
        elapsed = timeit.default_timer() - start
        total2 += elapsed
        data2.append(elapsed)

    plt.plot(lengths, data1, color='red', label='bubble_sort')
    plt.plot(lengths, data2, color='darkred', label='bubble_sort2')

    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime')
    plt.legend()

    plt.show()

    lengths = [2**x for x in range(13)]
    max_value = 2**30
    lists = [create_random_list(_, max_value) for _ in lengths]

    n = len(lengths)
    total1, total2, total3 = 0, 0, 0
    data1, data2, data3 = [], [], []
    cmp1, cmp2, cmp3 = [], [], []
    value = random.randint(0, max_value)

    for _ in range(n):
        print(_)
        L = lists[_]
        L1 = [*L]
        L2 = [*L]

        start = timeit.default_timer()
        selection_sort(L1)
        elapsed = timeit.default_timer() - start
        total1 += elapsed
        data1.append(elapsed)

        start = timeit.default_timer()
        selection_sort2(L2)
        elapsed = timeit.default_timer() - start
        total2 += elapsed
        data2.append(elapsed)

    plt.plot(lengths, data1, color='lime', label='selection_sort')
    plt.plot(lengths, data2, color='green', label='selection_sort2')

    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime')
    plt.legend()

    plt.show()

    lengths = [2**x for x in range(13)]
    max_value = 2**30
    lists = [create_random_list(_, max_value) for _ in lengths]

    n = len(lengths)
    total1, total2, total3 = 0, 0, 0
    data1, data2, data3 = [], [], []
    cmp1, cmp2, cmp3 = [], [], []
    value = random.randint(0, max_value)

    for _ in range(n):
        print(_)
        L = lists[_]
        L1 = [*L]
        L2 = [*L]

        start = timeit.default_timer()
        bubble_sort2(L1)
        elapsed = timeit.default_timer() - start
        total1 += elapsed
        data1.append(elapsed)

        start = timeit.default_timer()
        selection_sort2(L2)
        elapsed = timeit.default_timer() - start
        total2 += elapsed
        data2.append(elapsed)

    plt.plot(lengths, data1, color='darkred', label='bubble_sort2')
    plt.plot(lengths, data2, color='green', label='selection_sort2')

    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime')
    plt.legend()

    plt.show()

    #######
    #  3  #
    #######

    lengths = [2**x for x in range(13)]
    max_value = 2**30
    lists = [create_near_sorted_list(_, max_value, 0) for _ in lengths]

    n = len(lengths)
    total1, total2, total3 = 0, 0, 0
    data1, data2, data3 = [], [], []
    cmp1, cmp2, cmp3 = [], [], []
    value = random.randint(0, max_value)

    for _ in range(n):
        print(_)
        L = lists[_]
        L1 = [*L]
        L2 = [*L]
        L3 = [*L]

        start = timeit.default_timer()
        bubble_sort(L1)
        elapsed = timeit.default_timer() - start
        total1 += elapsed
        data1.append(elapsed)

        start = timeit.default_timer()
        insertion_sort(L2)
        elapsed = timeit.default_timer() - start
        total2 += elapsed
        data2.append(elapsed)

        start = timeit.default_timer()
        selection_sort(L3)
        elapsed = timeit.default_timer() - start
        total3 += elapsed
        data3.append(elapsed)

    print("Binary search avg runtime (ms): ", f"{total1/n:e}")
    print("Linear search avg runtime (ms): ", f"{total2/n:e}")

    plt.plot(lengths, data1, color='red', label='near_sorted_bubble_sort')
    plt.plot(lengths, data2, color='blue', label='near_sorted_insertion_sort')
    plt.plot(lengths, data3, color='lime', label='near_sorted_selection_sort')

    plt.title('Runtime Comparison of Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime')
    plt.legend()

    plt.show()
