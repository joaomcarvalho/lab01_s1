def maximo(array):
	max = array[0]
	for i in range (len(max)):
		if (max < array[i]):
			max = array[i]
	return max
