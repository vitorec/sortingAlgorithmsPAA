import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os


class DataPlot:
	"""
	This class generates the charts of results
	"""

	times = []
	comparisons = []
	swaps = []
	operations = {
		'comparisons': [],
		'swaps': []
	}
	labels = ['Insertion', 'Shellsort', 'Shellsort Otimizado', 'Quicksort', 'Heapsort', 'Mergesort']
	sizes = [25, 500]
	subtitle_labels = {
		'empty': 'Tempo de execução para registros pequenos',
		'filled': 'Tempo de execução para registros grandes'
	}
	axes_labels = {
		'ascending': 'Ordem crescente',
		'descending': 'Ordem decrescente',
		'random': 'Ordem aleatória'
	}
	y_labels = {
		'comparisons': 'Número de comparações',
		'swaps': 'Número de trocas'
	}

	def __init__(self, order, mode):
		self.order = order
		self.mode = mode

	def read_data(self, data_type='times', type=float):
		"""
		Read the results data
		:param data_type: {'times', 'comparisons', 'swaps'}
		:param type: {int, float}. A numeric primitive type
		:return: array. A two-dimensional array
		"""
		f = open("results/" + data_type + "_" + self.order + "_" + self.mode + ".txt", 'r')

		data = []
		line = f.readline()
		method = line.split()[0]

		method_data = []
		while line:
			if method != line.split()[0]:
				data.append(method_data)
				method = line.split()[0]
				method_data = []
			mean = type(line.split()[2])
			method_data.append(mean)
			line = f.readline()
		data.append(method_data)
		f.close()
		return data

	def load_data(self):
		"""
		Loads all the results data
		"""
		self.times = self.read_data('times', float)
		self.operations['comparisons'] = self.read_data('comparisons', int)
		self.operations['swaps'] = self.read_data('swaps', int)

	def plot_times(self):
		fig, ax = plt.subplots()
		plt.figure(figsize=(11, 4.7), dpi=100)

		# Título do gráfico
		fig.suptitle(self.subtitle_labels[self.mode])

		# Configuração dos eixos
		ax.set_xscale('log')
		ax.set_yscale('log')
		ax.set_xlabel('N')
		ax.set_ylabel('Segundos')
		ax.set_title(self.axes_labels[self.order], fontsize='small')
		ax.set_xticks(self.sizes)
		ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
		ax.grid()

		# Plotagem
		for t in self.times:
			ax.plot(self.sizes, t)

		# Legenda do gráfico
		ax.legend(self.labels, loc=2, fontsize='small', fancybox=True)

		plt.show()
		# os.chdir()

		# plt.savefig('times_' + self.order + '_' + self.mode + ".png")

	def plot_operations(self, type):
		men_means, men_std = (20, 35, 30, 35, 27), (2, 3, 4, 1, 2)
		women_means, women_std = (25, 32, 34, 20, 25), (3, 5, 2, 3, 3)
		values = self.operations[type]

		ind = np.arange(len(men_means))  # the x locations for the groups

		ind = np.arange(len(values))  # the x locations for the groups
		print(values)
		print(ind)
		width = 0.35  # the width of the bars

		fig, ax = plt.subplots()
		# rects1 = ax.bar(ind - width / 2, men_means, width, yerr=men_std, label='Men')
		# rects2 = ax.bar(ind + width / 2, women_means, width, yerr=women_std, label='Women')

		rects = []
		for v in values:
			rects.append(ax.bar(ind, v, width))
		# rects1 = ax.bar(ind - width / 2, men_means, width, yerr=men_std, label='Men')
		# rects2 = ax.bar(ind + width / 2, women_means, width, yerr=women_std, label='Women')
		# 			bar(x + i * dimw, y, dimw, bottom=0.001)
		# ax.bar()

		# Add some text for labels, title and custom x-axis tick labels, etc.
		ax.set_ylabel('Scores')
		ax.set_title('Scores by group and gender')
		ax.set_xticks(ind)
		# ax.set_yscale('log')
		# ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
		ax.set_xticklabels(self.sizes)
		ax.legend()


		# self.autolabel(ax, rects1, "left")
		# self.autolabel(ax, rects2, "right")

		plt.show()

	def autolabel(self, ax, rects, xpos='center'):
		"""
		Attach a text label above each bar in *rects*, displaying its height.

		*xpos* indicates which side to place the text w.r.t. the center of
		the bar. It can be one of the following {'center', 'right', 'left'}.
		"""

		xpos = xpos.lower()  # normalize the case of the parameter
		ha = {'center': 'center', 'right': 'left', 'left': 'right'}
		offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}

		for rect in rects:
			height = rect.get_height()
			ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
					'{}'.format(height), ha=ha[xpos], va='bottom', fontsize='x-small')
