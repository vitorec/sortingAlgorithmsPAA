"""
This module implements the most well-known sort algorithms
"""

import sys
from math import ceil

comparisons, swaps = 0, 0
sys.setrecursionlimit(1000000)


def insertion(list):
	global comparisons, swaps
	comparisons, swaps = 0, 0
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
	return comparisons, swaps


def shellsort(list):
	global comparisons, swaps
	comparisons, swaps = 0, 0
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
	return comparisons, swaps


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
	comparisons, swaps = 0, 0
	comparisons, swaps = shellsort_helper(list, gaps_function=tokuda_gaps)
	return comparisons, swaps


def shellsort_helper(list, gaps_function=tokuda_gaps):
	global comparisons, swaps
	n = len(list)
	gaps = gaps_function(n)
	for h in gaps:
		for i in range(h, n):
			r = list[i]
			j = i
			while list[j - h].key > r.key and j >= h:
				list[j] = list[j - h]
				j -= h
				comparisons += 1
				swaps += 1
			list[j] = r
			swaps += 1
	return comparisons, swaps


def quicksort(list):
	global comparisons, swaps
	comparisons, swaps = 0, 0
	quicksort_helper(list, 0, len(list) - 1)
	return comparisons, swaps


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


def heapsort(list):
	pass


def mergesort(list):
	pass

