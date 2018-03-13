
from math import ceil


def insertion(list):
	comparisons, swaps = 0, 0
	n = len(list)
	for i in range(1, n):
		r = list[i]
		j = i - 1
		while j >= 0 and list[j].key > r.key:
			list[j + 1] = list[j]
			j -= 1
			comparisons += 1
			swaps += 1
		list[j + 1] = r
		swaps += 1
	return comparisons, swaps


def shellsort(list):
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
			while list[j - h].key > r.key and j >= h:
				list[j] = list[j - h]
				j -= h
				# comparisons += 1
				# swaps += 1
			list[j] = r
			# swaps += 1
	return comparisons, swaps


def better_shellsort(list, gaps_function):
	comparisons, swaps = 0, 0
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


def tokuda_gaps(n):
	h, k = 1, 2
	gaps = []
	while h < n:
		gaps = [h] + gaps
		h = ceil((9 * pow(2.25, (k-1)) - 4) / 5)
		k += 1
	return gaps


def quicksort(list, left, right):
	if left < right:
		p = partition(list, left, right)
		quicksort(list, left, p - 1)
		quicksort(list, p + 1, right)


def partition(list, left, right):
	pivot = list[right].key
	i = left - 1
	for j in range(left, right):
		if list[j].key < pivot:
			i += 1
			swap(list, i, j)
	if list[right].key < list[i + 1].key:
		swap(list, i + 1, right)
	return i + 1


def swap(list, i, j):
	aux = list[i]
	list[i] = list[j]
	list[j] = aux


def heapsort(list):
	pass


def mergesort(list):
	pass

