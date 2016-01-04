import matplotlib.pyplot as plt
from pisanogenerator import pisano
import sys

start_value = 20 # must be > 0
end_value = 60

lengths = []
zeroes = []
for i in range(start_value, end_value + 1):
	print('Sets completed: ' + str(i - start_value) + 
		'/' + str(end_value-start_value))
	sys.stdout.write("\033[F") 
	pisano_set = pisano(i)
	lengths.append(len(pisano_set[0]))
	zeroes.append(pisano_set[1])

print('\nPlotting...')
plt.plot(range(start_value,end_value + 1), lengths)
plt.show()