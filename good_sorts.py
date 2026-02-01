"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""

import matplotlib
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
import math
from bad_sorts import insertion_sort2  # imported for experiment 8
from graph_algo import graph # imported for experiments 7 and 8

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

def bottom_up_mergesort_merge(arr, low1, high1, low2, high2): #LOOK HERE
    i = low1
    j = low2

    sorted = []

    while i <= high1 and j <= high2:
        if arr[i] <= arr[j]:
            sorted.append(arr[i])
            i += 1
        else:
            sorted.append(arr[j])
            j += 1

    while i <= high1:
        sorted.append(arr[i])
        i += 1

    while j <= high2:
        sorted.append(arr[j])
        j += 1

    k = low1
    for i in range(len(sorted)):
        arr[k] = sorted[i]
        k += 1


def bottom_up_mergesort(arr): # LOOK HERE
    size = 1
    n = len(arr)

    while size < n:
        low1 = 0
        while low1 < n:
            mid = min(low1 + size - 1, n - 1)
            high2 = min(low1 + 2 * size - 1, n - 1)
            bottom_up_mergesort_merge(arr, low1, mid, mid + 1, high2)
            low1 += size * 2
        size *= 2

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

if __name__ == "__main__":
    # *************************************
        
    # Experiment 3 
        
    def create_random_list(length, max_value):
        return [random.randint(0, max_value) for _ in range(length)]

    lengths = [2**x for x in range(13)]
    max_value = 2**30
    lists = [create_random_list(_, max_value) for _ in lengths]

    n = len(lengths)
    data1, data2, data3 = [], [], []
    value = random.randint(0, max_value)

    runs = 10

    for _ in range(n):
        total1, total2, total3 = 0, 0, 0
        trial1, trial2, trial3 = [],[],[]
        
        for i in range(runs):
            print(_)
            L = lists[_]
            L1 = [*L]
            L2 = [*L]
            L3 = [*L]

            start = timeit.default_timer()
            quicksort(L1)
            elapsed = timeit.default_timer() - start
            total1 += elapsed
            trial1.append(elapsed)

            start = timeit.default_timer()
            mergesort(L2)
            elapsed = timeit.default_timer() - start
            total2 += elapsed
            trial2.append(elapsed)

            start = timeit.default_timer()
            heapsort(L3)
            elapsed = timeit.default_timer() - start
            total3 += elapsed
            trial3.append(elapsed)
        
        data1.append(sum(trial1) / runs)
        data2.append(sum(trial2) / runs)
        data3.append(sum(trial3) / runs)


    for i in range(n):
        print(f"Run Size: {lengths[i]}:")
        print(f"  QuickSort: {data1[i]}")
        print(f"  MergeSort: {data2[i]}")
        print(f"  HeapSort: {data3[i]}")
        print(f"Performance Comparison: ")
        print(f"  QuickSort vs MergeSort : {round((data2[i] / data1[i]),2)}x")
        print(f"  QuickSort vs HeapSort : {round((data3[i] / data1[i]),2)}x")


    plt.plot(lengths, data1, color='red', label='quick_sort')
    plt.plot(lengths, data2, color='blue', label='merge_sort')
    plt.plot(lengths, data3, color='lime', label='heap_sort')

    plt.title('Runtime Comparison of Good Sorting Algorithms')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime')
    plt.legend()

    plt.show()


    # *************************************
    # Graphing of Experiment 7 and 8

    # mergesort and bottom_up_merge sort comparisons

    expertiment7_test_datas = [ 
        create_random_list(100, 40), # a list of 100 elements in range 0 ... 40
        create_random_list(1000, 1000), # a list of 1000 elements in range 0 ... 1000
        create_random_list(70000, 1000), # a list of 10000 elements in range 0 ... 1000
        create_random_list(200000, 100000), # a list of 100000 elements in range 0 ... 100000
        create_random_list(400000, 100000), # a list of 200000 elements in range 0 ... 100000
    ]

    graph(mergesort, bottom_up_mergesort, filePath="./Graphs/experiment7.png",
          title = 'Runtime Comparison of top down and bottom up merge sort', 
          colors = ("r", "b"), datas= expertiment7_test_datas
    )

    expertiment8_test_datas = [ 
        create_random_list(10, 10), # a list of 10 elements in range 0 ... 10
        create_random_list(20, 70), # a list of 20 elements in range 0 ... 70
        create_random_list(50, 100), # a list of 50 elements in range 0 ... 100
        create_random_list(70, 100), # a list of 70 elements in range 0 ... 100
        create_random_list(100, 100), # a list of 100 elements in range 0 ... 100
    ]

    graph(mergesort, quicksort, insertion_sort2, filePath="./Graphs/experiment8.png",
          title = 'Runtime Comparison of Insertion, Merge, and Quicksort', 
          colors = ("r", "b", "g"), datas= expertiment8_test_datas
    )

