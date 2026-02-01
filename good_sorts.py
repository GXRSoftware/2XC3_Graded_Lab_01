"""
Functionality Imported from bad_sorts.py
"""
import random
import math
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


# ******************* Bubble Sort *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

# Optimized Bubble sort
def bubble_sort2(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                temp = L[j+1]                  #LOOK HERE
                k = j
                while k >= 0 and L[k] > temp:  #LOOK HERE
                    L[k+1] = L[k]
                    k -= 1
                L[k+1] = temp                  #LOOK HERE 
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
        if (i == max_index):                          #LOOK HERE
            swap(L, i, min_index)
        else:
            swap(L, i, min_index)
            swap(L, l, max_index)                     #LOOK HERE
        i += 1
        l -= 1

def find_indexes(L, n, e):
    min_index = n
    max_index = n                                     #LOOK HERE
    for i in range(n+1, e + 1):
        if L[i] < L[min_index]:
            min_index = i
        if L[i] > L[max_index]:                       #LOOK HERE
            max_index = i
    return min_index, max_index


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

# ************ Dual Quick Sort ************
def dual_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]                                 #LOOK HERE
    pivot2 = L[1]                                 #LOOK HERE
    if pivot1 > pivot2:                           #LOOK HERE
        pivot1, pivot2 = pivot2, pivot1
    left, mid, right = [], [], []                 #LOOK HERE
    for num in L[2:]:
        if num < pivot1:                          #LOOK HERE
            left.append(num)
        elif num < pivot2:                        #LOOK HERE
            mid.append(num)
        else:                                     #LOOK HERE
            right.append(num)
    return dual_quicksort_copy(left) + [pivot1] + dual_quicksort_copy(mid) + [pivot2] + dual_quicksort_copy(right)

# *************************************

# ************ n Quick Sort (requires insertion sort for pivots, due to short list) ************
def n_quicksort(L, n):
    copy = n_quicksort_copy(L, n)
    for i in range(len(L)):
        L[i] = copy[i]


def n_quicksort_copy(L, n):
    l = len(L)
    if l < 2:
        return L
    if (n > l):
        n = l

    pivots = [L[i] for i in range(0, n)]            #LOOK HERE
    insertion_sort(pivots)

    divs = [[] for i in range(n + 1)]               #LOOK HERE

    for num in L[n:]:
        i = 0
        added = False                               #LOOK HERE
        while i < n:                                #LOOK HERE
            if num < pivots[i]:                     #LOOK HERE
                added = True
                divs[i].append(num)
                i = n
            i += 1
        if not added:                               #LOOK HERE
            divs[n].append(num)
   
    r = n_quicksort_copy(divs[0], n)                #LOOK HERE
    for i in range(n):                              #LOOK HERE
        r.append(pivots[i])
        r.extend(n_quicksort_copy(divs[i + 1], n))

    return r

# *************************************

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

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

# ******************
# ** Experiment 4 **
# ******************
    
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

# ===============================================================
# Experiment 5: swaps vs time (quicksort vs mergesort vs heapsort)
# ===============================================================
import sys
sys.setrecursionlimit(30000)

RUNS = 10
LIST_LENGTH = 2**12          # constant list length for this experiment
MAX_VALUE = 2**30

# choose a swaps range (more resolution at the small end helps)
swap_counts = list(range(0, 33)) + [40, 50, 60, 75, 100, 150, 200, 300, 400, 600, 800, 1000]

times_q, times_m, times_h = [], [], []

for s in swap_counts:
    # average over RUNS; generate a fresh near-sorted list each run
    tq = tm = th = 0.0

    for _ in range(RUNS):
        base = create_near_sorted_list(LIST_LENGTH, MAX_VALUE, s)

        L1 = base[:]
        start = timeit.default_timer()
        quicksort(L1)
        tq += (timeit.default_timer() - start)

        L2 = base[:]
        start = timeit.default_timer()
        mergesort(L2)
        tm += (timeit.default_timer() - start)

        L3 = base[:]
        start = timeit.default_timer()
        heapsort(L3)
        th += (timeit.default_timer() - start)

    times_q.append(tq / RUNS)
    times_m.append(tm / RUNS)
    times_h.append(th / RUNS)

plt.plot(swap_counts, times_q, label="quicksort")
plt.plot(swap_counts, times_m, label="mergesort")
plt.plot(swap_counts, times_h, label="heapsort")
plt.title(f"Swaps vs Time")
plt.xlabel("Number of swaps")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()


# ===============================================================
# Experiment 6: list length vs time (quicksort vs dual_quicksort)
# ===============================================================

RUNS = 10
MAX_VALUE = 2**30
lengths = [2**x for x in range(5, 15)]  # 32 .. 16384

times_q2, times_dq = [], []

for n in lengths:
    tq = td = 0.0

    for _ in range(RUNS):
        base = create_random_list(n, MAX_VALUE)

        L1 = base[:]
        start = timeit.default_timer()
        quicksort(L1)
        tq += (timeit.default_timer() - start)

        L2 = base[:]
        start = timeit.default_timer()
        dual_quicksort(L2)
        td += (timeit.default_timer() - start)

    times_q2.append(tq / RUNS)
    times_dq.append(td / RUNS)

plt.plot(lengths, times_q2, label="quicksort")
plt.plot(lengths, times_dq, label="dual_quicksort")
plt.title(f"List Length vs Time")
plt.xlabel("List length")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()

# ===============================================================
# Additional
# ===============================================================

import timeit
import matplotlib.pyplot as plt

RUNS = 10
MAX_VALUE = 2**30
lengths = [2**x for x in range(5, 15)]  # 32 .. 16384
ns = [1, 2, 3, 4, 5]

results = {n: [] for n in ns}

for length in lengths:
    base = create_random_list(length, MAX_VALUE)

    for n in ns:
        elapsed = 0.0
        for _ in range(RUNS):
            L = base[:]
            start = timeit.default_timer()
            n_quicksort(L, n)
            elapsed += timeit.default_timer() - start
        results[n].append(elapsed / RUNS)

for n in ns:
    plt.plot(lengths, results[n], label=f"n_quicksort (n={n})")

plt.title(f"n-QuickSort Comparison")
plt.xlabel("List length")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()

