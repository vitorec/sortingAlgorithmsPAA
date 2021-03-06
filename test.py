import os
import sys
import time
import sorting
import numpy as np
from math import ceil

sys.setrecursionlimit(1000000)


def run_test(method, factory):
	times_list = []
	comparisons_list = []
	swaps_list = []
	executions = 10
	for i in range(executions):
		list = factory.make_list()

		start_time = time.clock()
		sorting.comparisons, sorting.swaps = 0, 0
		method(list)
		seconds = time.clock() - start_time

		times_list.append(seconds)
		comparisons_list.append(sorting.comparisons)
		swaps_list.append(sorting.swaps)

	data = {
		'n': factory.n,
		'method': str(method).split(' ')[1],
		'mode': factory.mode,
		'order': factory.order,
		'times': {
			'min': str('{:.15f}'.format(np.min(times_list))),
			'max': str('{:.15f}'.format(np.max(times_list))),
			'mean': str('{:.15f}'.format(np.mean(times_list)))
		},
		'comparisons': {
			'min': np.min(comparisons_list),
			'max': np.max(comparisons_list),
			'mean': ceil(np.mean(comparisons_list))
		},
		'swaps': {
			'min': np.min(swaps_list),
			'max': np.max(swaps_list),
			'mean': ceil(np.mean(swaps_list))
		},
	}
	return data


def write_result_line(data):
	try:
		os.mkdir('results')
	except OSError:
		print("\to diretorio ja existe")

	f = open("results/times_" + data['order'] + "_" + data['mode'] + ".txt", 'a')
	f.write('%s\t%s\t%s\t%s\t%s\n' % (
		data['method'],
		data['n'],
		data['times']['mean'],
		data['times']['min'],
		data['times']['max']))
	f.close()

	f = open("results/comparisons_" + data['order'] + "_" + data['mode'] + ".txt", 'a')
	f.write('%s\t%s\t%s\t%s\t%s\n' % (
		data['method'],
		data['n'],
		data['comparisons']['mean'],
		data['comparisons']['min'],
		data['comparisons']['max']))
	f.close()

	f = open("results/swaps_" + data['order'] + "_" + data['mode'] + ".txt", 'a')
	f.write('%s\t%s\t%s\t%s\t%s\n' % (
		data['method'],
		data['n'],
		data['swaps']['mean'],
		data['swaps']['min'],
		data['swaps']['max']))
	f.close()
