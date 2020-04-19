def Grad():
	humans = Human()

	human11 = np.gradient(toList(open("./s3/1.pgm").resize([10,10])))
	human12 = np.gradient(toList(open("./s3/2.pgm").resize([10,10])))
	human21 = np.gradient(toList(open("./s36/3.pgm").resize([10,10])))

	fig = plt.figure()
	plt.plot(range(len(human11)),human11, color='g', linewidth=1, drawstyle='steps-pre')
	plt.show()

	print(distanceBetween(toDFTvectorDynamic(humans[2], 10)[0], toDFTvectorDynamic(humans[2], 10)[1]))

	plt.plot(range(len(human12)),human12, color='g', linewidth=1, drawstyle='steps-pre')
	plt.show()

	print(distanceBetween(toDFTvectorDynamic(humans[2], 10)[1], toDFTvectorDynamic(humans[35], 10)[2]))

	plt.plot(range(len(human21)),human21, color='g', linewidth=1, drawstyle='steps-pre')
	plt.show()