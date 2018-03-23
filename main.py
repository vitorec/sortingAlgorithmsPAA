#!/usr/bin/python

import test
import time
import sort_helper as sorting
from factory import Factory
from dataplot import DataPlot

sizes = [25, 500, 10000, 200000, 1000000]
orders = ['descending', 'random', 'ascending']
modes = ['filled', 'empty']
operations = ['comparisons', 'swaps']


def plot_charts():
	for order in orders:
		dataplot = DataPlot(order, modes[0], sizes)
		dataplot.load_data()
		dataplot.plot_times()
		for operation in operations:
			dataplot.plot_operations(operation)


def run_all():
	start = time.time()
	for mode in modes:
		for order in orders:
			for sort in sorting.__all__:
				for n in sizes:
					factory = Factory(n, order=order, mode=mode)
					data = test.run_test(sort, factory)
					try:
						test.write_result_line(data)
					except Exception:
						print('data: \n', data)

				print('%s concluido' % str(sort).split(' ')[1])
			print('%s concluido' % order)
		print('%s concluido' % mode)
	end = time.time() - start
	print('Concluído')
	print("Tempo total: %s segundos ---" % end)


if __name__ == '__main__':

	# Run all the algorithms
	run_all()

	# Plot all the charts
	plot_charts()




