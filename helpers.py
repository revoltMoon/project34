def open(name):
	img = Image.open(name)
	t = img.copy()
	img.close()
	return t

def toList(image):
	return list(image.getdata())

def toArray(matrix):
	vector = []

	for i in range(len(matrix)):
		for y in range(len(matrix[0])):
			vector.append(matrix[i][y])

	return vector

def human(number):
	human= [0] * 10 
	for j in range(10):
		human[j] = open("./s" + str(number+1) + "/" + str(j+1) + ".pgm")
	return human

def convert(image):
	pixels = list(image.getdata())
	width, height = image.size
	pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
	return pixels

def Human():

	human = []

	for h in range(1,41):
		person = []
		for j in range(1,11):
			person.append(open("./s" + str(h) + "/" + str(j) + ".pgm"))
		human.append(person)

	return human


def distanceBetween(vec1, vec2):
	return distance.euclidean(vec1, vec2)

# Functions for histogram

def toHistogramVector(human):
	vectors = []
	for item in range(len(human)):
		vectors.append(human[item].histogram())
	return vectors

def compression(histogram, size):
	lenght = len(histogram)

	quantity = math.trunc(lenght/size)

	list = []

	start = 0

	for item in range(size-1):
		list.append(sum(histogram[start:start+quantity]))
		start=start + quantity
	list.append(sum(histogram[quantity*(size-1):lenght-1]))

	return list

def toHistogramVectorDynamic(human, size):
	vectors = []
	human = toHistogramVector(human)
	for item in range(len(human)):
		vectors.append(compression(human[item],size))
	return vectors

# / Functions for histogram

# Functions for Points

# Function for get Random coordinates of 200 points
def getRandomPoints():

	points = []
	for point in range(250):
		x = random.randint(0,111)
		y = random.randint(0,91)
		points.append([x,y])

	return points

# Get specially points of image
def getPointsFromHuman(human, coordinates):
	vector = []

	for point in coordinates:
		vector.append(human[point[0]][point[1]])

	return vector

def toRandomDynamic(human, quantity):
	vectors = []

	for person in human:
		vectors.append(getPointsFromHuman(convert(person), points[0:quantity]))

	return vectors
#/ Functions for Points

# Functions for Scale
def toScaleVector(human):
	vecHuman = []

	for hum in human:
		vecHuman.append(toList(hum.resize([69, 84])))   #75%

	return vecHuman

def toScaleVectorDynamic(human, size):
	vecHuman = []

	h = math.trunc(92*size)
	w = math.trunc(122*size)

	for hum in human:
		vecHuman.append(toList(hum.resize([h,w])))

	return vecHuman

#/ Functions for Scale

# Functions for DCT

def toDCTvectorDynamic(human, n):
	vecHuman = []

	for hum in human:
		vecHuman.append(dct(toList(hum.resize([n,n])), axis=0))

	return vecHuman

#/ Functions for DCT

# Functions for DFT
def toDFTvectorDynamic(human, n):
	vecHuman = []


	for hum in human:
		vecHuman.append(fft(toList(hum.resize([n,n])), axis=0))

	return vecHuman

#/ Functions for DFT

# Functions for Grad

def toGradVectorDynamicList(human, n):
	vecHuman = []

	for hum in human:
		vecHuman.append(np.gradient(toList(hum.resize([n,n]))))

	return vecHuman

#/ Functions for Grad

def Persent(arrFalse, arrTrue):
	result = []

	q = len(arrFalse)

	for index in range(q):
		if (arrFalse[index] < arrTrue[index]):
			result.append(index)

	return (q-len(result))/q*100