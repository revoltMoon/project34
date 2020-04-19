def DCT():
	humans = Human()

	human11 = dct(convert(open("./s29/5.pgm").resize([12,12])))
	human12 = dct(convert(open("./s29/6.pgm").resize([12,12])))
	human21 = dct(convert(open("./s31/2.pgm").resize([12,12])))

	fig = plt.figure()
	plt.imshow(human11, interpolation='nearest', cmap = 'gray')
	plt.show()

	print(distanceBetween(toDCTvectorDynamic(humans[28], 12)[4], toDCTvectorDynamic(humans[9], 12)[6]))

	plt.imshow(human12, interpolation='nearest', cmap = 'gray')
	plt.show()

	print(distanceBetween(toDCTvectorDynamic(humans[28], 12)[4], toDCTvectorDynamic(humans[39], 12)[1]))

	plt.imshow(human21, interpolation='nearest', cmap = 'gray')
	plt.show()