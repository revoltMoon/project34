def DFT():
	humans = Human()

	human11 = fft(convert(open("./s33/2.pgm").resize([16,16])))
	human12 = fft(convert(open("./s33/4.pgm").resize([16,16])))
	human21 = fft(convert(open("./s25/2.pgm").resize([16,16])))

	fig = plt.figure()
	plt.imshow(np.abs(human11), interpolation='nearest', cmap = 'gray')
	plt.show()

	print(distanceBetween(toDFTvectorDynamic(humans[9], 16)[1], toDFTvectorDynamic(humans[9], 16)[3]))

	plt.imshow(np.abs(human12), interpolation='nearest', cmap = 'gray')
	plt.show()

	print(distanceBetween(toDFTvectorDynamic(humans[9], 16)[1], toDFTvectorDynamic(humans[26], 16)[1]))

	plt.imshow(np.abs(human21), interpolation='nearest', cmap = 'gray')
	plt.show()