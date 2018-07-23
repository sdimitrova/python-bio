import matplotlib.pylab as plt
import random
SAMPLE_SIZE = 100
# seed random generator
# if no argument provided
# uses system current time
random.seed()
# store generated random values here
real_rand_vars = []
# pick some random values
real_rand_vars = [random.random() for val in range(SAMPLE_SIZE)]
# create histogram from data in 10 buckets
plt.hist(real_rand_vars, 10)
# define x and y labels
plt.xlabel("Number range")
plt.ylabel("Count")
# show figure
plt.show()