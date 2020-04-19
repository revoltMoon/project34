def Scale():
	humans = Human()

	h = math.trunc(92*0.4)
	w = math.trunc(112*0.4)

	human11 = open("./s13/1.pgm").resize([h,w])
	human12 = open("./s13/5.pgm").resize([h,w])
	human21 = open("./s40/3.pgm").resize([h,w])

	fig = plt.figure()
	plt.imshow(human11, cmap = 'gray')
	plt.show()

	print(distanceBetween(toScaleVectorDynamic(humans[12], 0.4)[0], toScaleVectorDynamic(humans[12], 0.4)[4]))

	plt.imshow(human12, cmap = 'gray')
	plt.show()

	print(distanceBetween(toScaleVectorDynamic(humans[12], 0.4)[0], toScaleVectorDynamic(humans[39], 0.4)[2]))

	plt.imshow(human21, cmap = 'gray')
	plt.show()