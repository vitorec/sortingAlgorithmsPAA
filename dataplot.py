from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


class DataPlot:
	"""
	This class generates the charts of results
	"""

	times = {
		'empty': [],
		'filled': []
	}

	comparisons = []

	swaps = []

	operations = {
		'comparisons': {
			'empty': [],
			'filled': []
		},
		'swaps': {
			'empty': [],
			'filled': []
		},
	}

	columns = ['N', 'quicksort', 'heapsort', 'mergesort', 'better_shellsort', 'shellsort', 'insertion']

	labels = ['Quicksort', 'Heapsort', 'Mergesort', 'Shellsort Otimizado', 'Shellsort', 'Insertion']
	# sizes = [25, 500, 10000, 200000, 1000000]
	# sizes = [25, 500]

	axes_labels = {
		'empty': 'Registros pequenos',
		'filled': 'Registros grandes'
	}

	subtitle_labels = {
		'ascending': 'Tempo de execução para array em ordem crescente',
		'descending': 'Tempo de execução para array em ordem decrescente',
		'random': 'Tempo de execução para array em ordem aleatória'
	}

	y_labels = {
		'comparisons': 'Número de comparações',
		'swaps': 'Número de trocas'
	}

	bar_title_labels = {
		'ascending': {
			'comparisons': 'Número de comparações para array em ordem crescente',
			'swaps': 'Número de trocas para array em ordem crescente'
		},
		'descending': {
			'comparisons': 'Número de comparações para array em ordem decrescente',
			'swaps': 'Número de trocas para array em ordem decrescente'
		},
		'random': {
			'comparisons': 'Número de comparações para array em ordem aleatória',
			'swaps': 'Número de trocas para array em ordem aleatória'
		}
	}

	def __init__(self, order, mode, sizes):
		"""

		:param order: {'ascending', 'descending', 'random'}. The order of the data
		:param mode: {'empty', 'filled'}. The type of the records
		:param sizes: array. An array of the sizes of N
		"""
		self.order = order
		self.mode = mode
		self.sizes = sizes

	def read_data(self, data_type='times', mode='empty'):
		"""
		Read the results data
		:param data_type: {'times', 'comparisons', 'swaps'}.
		:param mode: {'empty', 'filled'}. The type of the records
		:return: array. A two-dimensional array
		"""
		f = open("results/" + data_type + "_" + self.order + "_" + mode + ".txt", 'r')

		data = []
		line = f.readline()
		method = line.split()[0]

		method_data = []
		if data_type != 'times':
			method_data = str(self.sizes).strip('[]')

		while line:
			if method != line.split()[0]:
				data.append(method_data)
				method = line.split()[0]
				method_data = []
			mean = float(line.split()[2])
			method_data.append(mean)
			line = f.readline()
		data.append(method_data)
		f.close()
		return data

	def read_operations(self, data_type='comparisons', mode='empty'):
		"""
		Read the results data
		:param data_type: {'times', 'comparisons', 'swaps'}
		:param mode: {'empty', 'filled'}. The type of the records
		:return: array. A two-dimensional array
		"""
		f = open("results/" + data_type + "_" + self.order + "_" + mode + ".txt", 'r')

		values = []
		for line in f:
			method = line.split()[0]
			mean = float(line.split()[2])
			values.append((method, mean))
		f.close()

		data = defaultdict(list)
		data['N'] = self.sizes
		for method, mean in values:
			data[method].append(mean)

		return data

	def load_data(self):
		"""
		Loads all the results data
		"""
		self.times['empty'] = self.read_data('times', 'empty')
		self.times['filled'] = self.read_data('times', 'filled')
		comparisons = {
			'empty': self.read_operations('comparisons', 'empty'),
			'filled': self.read_operations('comparisons', 'filled'),
		}
		swaps = {
			'empty': self.read_operations('swaps', 'empty'),
			'filled': self.read_operations('swaps', 'filled'),
		}
		self.operations['comparisons'] = comparisons
		self.operations['swaps'] = swaps

	def plot_times(self):
		"""
		Plot the line charts of times
		"""

		fig = plt.figure(figsize=(11, 4.7), dpi=100)

		# Título do gráfico
		fig.suptitle(self.subtitle_labels[self.order])

		fig.subplots_adjust(left=0.06, bottom=0.12, right=0.98, top=0.88, wspace=0.20, hspace=0.40)

		# Configuração dos eixos
		ax1 = fig.add_subplot(121)
		ax2 = fig.add_subplot(122)

		ax1.set_xscale('log')
		ax1.set_yscale('symlog')
		ax1.set_xlabel('N')
		ax1.set_ylabel('Segundos')
		ax1.set_title(self.axes_labels['empty'], fontsize='medium')
		ax1.set_xticks(self.sizes)
		ax1.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
		ax1.grid(which='major', linestyle=':', linewidth=0.5, color='black', alpha=0.75)

		# Plotagem
		for t in self.times['empty']:
			ax1.plot(self.sizes, t, ls='-', lw=1.1, marker='.')

		ax2.set_xscale('log')
		ax2.set_yscale('symlog')
		ax2.set_xlabel('N')
		ax2.set_ylabel('Segundos')
		ax2.set_title(self.axes_labels['filled'], fontsize='medium')
		ax2.set_xticks(self.sizes)
		ax2.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
		ax2.grid(which='major', linestyle=':', linewidth=0.5, color='black', alpha=0.75)

		# Plotagem
		for t in self.times['filled']:
			ax2.plot(self.sizes[:len(self.times['filled'][0])], t, ls='-', lw=1.1, marker='.')

		# Legenda do gráfico
		ax1.legend(self.labels, loc=2, fontsize='small', fancybox=True)
		ax2.legend(self.labels, loc=2, fontsize='small', fancybox=True)

		plt.savefig('times_' + self.order + ".png")
		plt.show()

	def plot_operations(self, data_type):
		"""
		Plot the bar charts of comparisons and swaps
		:param data_type: {'comparisons', 'swaps'}. The type of data to plot
		"""

		fig = plt.figure(figsize=(11, 4.7), dpi=100)

		# Título do gráfico
		fig.suptitle(self.bar_title_labels[self.order][data_type])

		fig.subplots_adjust(left=0.06, bottom=0.12, right=0.98, top=0.88, wspace=0.20, hspace=0.40)

		df1 = pd.DataFrame(self.operations[data_type]['empty'], columns=self.columns)
		df2 = pd.DataFrame(self.operations[data_type]['filled'], columns=self.columns)

		pos = list(range(len(df1['quicksort'])))
		width = 0.12

		# Configuração dos eixos
		ax1 = fig.add_subplot(121)
		ax2 = fig.add_subplot(122)

		ax1.set_yscale('log')
		ax1.set_xlabel('N')
		ax1.set_xticklabels([0] + self.sizes)
		ax1.set_ylabel(self.y_labels[data_type])
		ax1.set_title(self.axes_labels['empty'], fontsize='medium')
		ax1.grid(which='major', linestyle=':', linewidth=0.5, color='black', alpha=0.75)

		# Plotagem
		for i in range(len(self.columns[1:])):
			position = [p + width * (i - 2) for p in pos]
			print(position)
			ax1.bar(position, df1.iloc[:,i+1], width, alpha=0.75, edgecolor='black', linewidth=0.75, bottom=0)
			i += 1

		ax2.set_yscale('log')
		ax2.set_xlabel('N')
		ax2.set_xticklabels([0] + self.sizes)
		ax2.set_ylabel(self.y_labels[data_type])
		ax2.set_title(self.axes_labels['filled'], fontsize='medium')
		ax2.grid(which='major', linestyle=':', linewidth=0.5, color='black', alpha=0.75)

		# Plotagem
		for i in range(len(self.columns[1:])):
			position = [p + width * (i - 2) for p in pos]
			ax2.bar(position, df2.iloc[:,i+1], width, alpha=0.75, edgecolor='black', linewidth=0.75, bottom=0)
			i += 1

		# Legenda do gráfico
		ax1.legend(self.labels, loc=2, fontsize='small', fancybox=True)
		ax2.legend(self.labels, loc=2, fontsize='small', fancybox=True)

		plt.savefig(data_type + '_' + self.order + ".png")
		plt.show()

