
# must be >= 2. if 2 return [0,1], 2
def pisano(divider):
	'''returns a tuple containing the pisano set as a list 
	and the number of zeroes in the set'''
	if divider == 1:
		return ([0], 1)

	pisano_set = [0, 1, 1]

	i = 2
	zeroes = 0
	while not (pisano_set[i-1] == 0 and pisano_set[i] == 1):
		number = pisano_set[i] + pisano_set[i-1]
		if number >= divider:
			number = number - divider
		if number == 0:
			zeroes += 1
		pisano_set.append(number)
		i += 1

	pisano_set = pisano_set[:-2]
	return (pisano_set, zeroes)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('divider', type=int, help="Number to divide the fibonacci sequence by")
	args = parser.parse_args()
	pisano_set = pisano(args.divider)
	print('Set: ' + str(pisano_set[0]))
	print('Length: ' + str(len(pisano_set[0])))
	print('Zeroes: ' + str(pisano_set[1]))