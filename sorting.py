"""
This module implements the most well-known sort algorithms
"""

import sys
from math import ceil

comparisons, swaps = 0, 0
sys.setrecursionlimit(1000000)


def insertion(list):
	global comparisons, swaps
	n = len(list)
	for i in range(1, n):
		r = list[i]
		j = i - 1
		comparisons += 1
		while j >= 0 and list[j].key > r.key:
			list[j + 1] = list[j]
			j -= 1
			comparisons += 1
			swaps += 1
		list[j + 1] = r
		swaps += 1


def shellsort(list):
	global comparisons, swaps
	h = 1
	n = len(list)
	for h in range(n):
		h = 3 * h + 1
	while h > 0:
		h //= 3
		for i in range(h, n):
			r = list[i]
			j = i
			comparisons += 1
			while list[j - h].key > r.key and j >= h:
				list[j] = list[j - h]
				j -= h
				comparisons += 1
				swaps += 1
			list[j] = r
			swaps += 1


def tokuda_gaps(n):
	h, k = 1, 2
	gaps = []
	while h < n:
		gaps = [h] + gaps
		h = ceil((9 * pow(2.25, (k-1)) - 4) / 5)
		k += 1
	return gaps


def better_shellsort(list):
	global comparisons, swaps
	shellsort_helper(list, gaps_function=tokuda_gaps)


def shellsort_helper(list, gaps_function=tokuda_gaps):
	global comparisons, swaps
	n = len(list)
	gaps = gaps_function(n)
	for h in gaps:
		for i in range(h, n):
			r = list[i]
			j = i
			comparisons += 1
			while list[j - h].key > r.key and j >= h:
				list[j] = list[j - h]
				j -= h
				comparisons += 1
				swaps += 1
			list[j] = r
			swaps += 1


def quicksort(list):
	global comparisons, swaps
	quicksort_helper(list, 0, len(list) - 1)


def quicksort_helper(list, left, right):
	i, j = partition(list, left, right)
	if left < j:
		quicksort_helper(list, left, j)
	if i < right:
		quicksort_helper(list, i, right)
	pass


def partition(list, left, right):
	global comparisons, swaps
	i, j = left, right
	pivot = list[(i + j) // 2].key
	while True:
		if j <= i:
			break
		comparisons += 1
		while pivot > list[i].key:
			i += 1
			comparisons += 1
		comparisons += 1
		while pivot < list[j].key:
			j -= 1
			comparisons += 1
		if i <= j:
			swap(list, i, j)
			swaps += 1
			i += 1
			j -= 1
	return i, j


def swap(list, i, j):
	aux = list[i]
	list[i] = list[j]
	list[j] = aux


def merge(a, b):
	global comparisons, swaps
	c = []
	while len(a) > 0 and len(b) > 0:
		comparisons += 2
		swaps += 1

		if a[0].key > b[0].key:
			c.append(b[0])
			b.pop(0)
		else:
			c.append(a[0])
			a.pop(0)

	comparisons += 1

	while len(a) > 0:
		comparisons += 1
		swaps += 1

		c.append(a[0])
		a.pop(0)

	comparisons += 1
	while len(b) > 0:
		comparisons += 1
		swaps += 1

		c.append(b[0])
		b.pop(0)

	return c


def mergesort(list):
	global comparisons, swaps

	comparisons += 1
	if len(list) < 2:
		return list

	a = list[:int(len(list)/2)]
	b = list[int(len(list)/2):]

	a = mergesort(a)
	b = mergesort(b)

	return merge(a,b)


def heapify(list, i, n):
	global comparisons, swaps

	left = 2 * i + 1
	right = 2 * i + 2
	max = i

	if (left < n) and (list[left].key > list[i].key):
		comparisons += 1
		max = left

	if (right < n) and (list[right].key > list[max].key):
		comparisons += 1
		max = right

	if (max != i):
		swaps += 1
		swap(list, i, max)
		heapify(list, max, n)


def heapsort(list):
	global comparisons, swaps

	n = len(list)

	for i in range(n, -1, -1):
		heapify(list, i, n)

	for i in range(n - 1, 0, -1):
		swaps += 1

		swap(list, 0, i)
		heapify(list, 0, i)

	return list

