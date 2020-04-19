def Histogram():
	humans = Human()
	human11 = open("./s2/5.pgm")
	human12 = open("./s2/7.pgm")
	human21 = open("./s12/9.pgm")
	fig = plt.figure()
	plt.bar(range(0,220), toHistogramVector(humans[2])[5], color='g')
	plt.show()

	plt.bar(range(0,220), toHistogramVector(humans[2])[7], color='g')
	print(distanceBetween(toHistogramVector(humans[2])[5],toHistogramVector(humans[2])[7]))
	plt.show()

	plt.bar(range(0,220), toHistogramVector(humans[12])[5], color='r')
	print(distanceBetween(toHistogramVector(humans[2])[5],toHistogramVector(humans[12])[5]))
	plt.show()

points = getRandomPoints()