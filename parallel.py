def parallel():
	humans = Human()
	points = getRandomPoints()

	sums = []
	persent = []

	vectorsHist = []
	vectorsRandom = []
	vectorsScale = []
	vectorsDCT = []
	vectorsDFT = []
	vectorsGrad = []

	for i in range(40):
		vectorsHist.append(toHistogramVectorDynamic(humans[i], 9))
		vectorsRandom.append(toRandomDynamic(humans[i], 90))
		vectorsScale.append(toScaleVectorDynamic(humans[i], 0.175))
		vectorsDCT.append(toDCTvectorDynamic(humans[i], 10))
		vectorsDFT.append(toDFTvectorDynamic(humans[i], 15))
		vectorsGrad.append(toGradVectorDynamicList(humans[i], 9))

	print("End of Vectors")

	for v in range(0,10):
		print(v)
		for d in range(1,41):
			persent.append(max(MainData(vectorsHist, v, d), MainData(vectorsRandom, v, d), MainData(vectorsScale, v, d), MainData(vectorsDCT, v, d), MainData(vectorsDFT, v, d), MainData(vectorsGrad, v, d)))
		sums.append(round(sum(persent)/len(persent), 2))
		persent = []

	fig = plt.figure()
	print(max(sums), sums.index(max(sums)))
	plt.plot(range(0,400, 20), sums, color='g', linewidth=1)
	plt.show()