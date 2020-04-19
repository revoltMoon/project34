
import math
import random
import numpy as np
from PIL import Image
from scipy import fft
from scipy.spatial import distance
from matplotlib import pyplot as plt
from scipy.fftpack import dct

def main(vectors, quantity, klass):

	minTrue = []
	minFalse = []

	for b in range(10-quantity):
		minTrue.append(distanceBetween(vectors[klass-1][0], vectors[klass-1][quantity+b]))
		minFalse.append(distanceBetween(vectors[random.randint(0,39)][0], vectors[klass-1][quantity+b]))

	for k in range(quantity,10):
		for s in range(0,quantity):
			if (distanceBetween(vectors[klass-1][k], vectors[klass-1][s]) < minTrue[k-quantity]):
				minTrue[k-quantity] = distanceBetween(vectors[klass-1][k], vectors[klass-1][s])

	for x in range(40):
		for y in range(10):
			if (x == klass - 1):
				break
			for h in range(10-quantity):
				if (distanceBetween(vectors[x][y], vectors[klass-1][h+quantity]) < minFalse[h]):
					minFalse[h] = distanceBetween(vectors[x][y], vectors[klass-1][h+quantity])

	return Persent(minFalse, minTrue)

def dataPersents(vectors, quantity, klass, size):

	minTrue = []
	minFalse = []

	for b in range(10-quantity):
		minTrue.append(distanceBetween(vectors[klass-1][0], vectors[klass-1][quantity+b]))
		minFalse.append(distanceBetween(vectors[random.randint(0,39)][0], vectors[klass-1][quantity+b]))

	for k in range(quantity,10):
		for s in range(0,quantity):
			if (distanceBetween(vectors[klass-1][k], vectors[klass-1][s]) < minTrue[k-quantity]):
				minTrue[k-quantity] = distanceBetween(vectors[klass-1][k], vectors[klass-1][s])

	for x in range(40):
		for y in range(10):
			if (x == klass - 1):
				break
			for h in range(10-quantity):
				if (distanceBetween(vectors[x][y], vectors[klass-1][h+quantity]) < minFalse[h]):
					minFalse[h] = distanceBetween(vectors[x][y], vectors[klass-1][h+quantity])

	return Persent(minFalse, minTrue)

def OptimalParam(toVectorDynamic, ranges):
	vectors = []

	persent = []
	sums = []

	humans = Human()

	for v in ranges:
		for i in range(40):
			vectors.append(toVectorDynamic(humans[i], v))
		for d in range(1,41):
			persent.append(CheckDataPersents(vectors, 9, d, v))
		sums.append(round(sum(persent)/len(persent), 2))
		print(v)
		persent = []
		vectors = []
	fig = plt.figure()
	plt.plot(ranges, sums, color='g', linewidth=1, drawstyle='steps-pre')
	plt.show()

def LastDef(toVectorDynamic, params):
	vectors = []

	persent = []
	sums = []

	humans = Human()

	for i in range(40):
		vectors.append(toVectorDynamic(humans[i], params))

	for v in range(0,10):
		for d in range(1,41):
			persent.append(CheckDataPersents(vectors, v, d, params))
		sums.append(round(sum(persent)/len(persent), 2))
		print(v)
		persent = []
	fig = plt.figure()
	print(max(sums), sums.index(max(sums)))
	plt.plot(range(0,400,40), sums, color='g', linewidth=1)
	plt.show()

def OptimalParams():
	OptimalParam(toHistogramVectorDynamic, range(2,220))
	points = getRandomPoints()
	OptimalParam(toRandomDynamic, range(1,150))
	OptimalParam(toScaleVectorDynamic, np.arange(0.05, 1, 0.05))
	OptimalParam(toDCTvectorDynamic, range(2,50))
	OptimalParam(toDFTvectorDynamic, range(2,50))
	OptimalParam(toGradVectorDynamicList, range(2, 100))

def LastParams():
	LastDef(toHistogramVectorDynamic, 9)
	points = getRandomPoints()
	LastDef(toRandomDynamic, 90)
	LastDef(toScaleVectorDynamic, 0.175)
	LastDef(toDCTvectorDynamic, 10)
	LastDef(toDFTvectorDynamic, 15)
	LastDef(toGradVectorDynamicList, 9)