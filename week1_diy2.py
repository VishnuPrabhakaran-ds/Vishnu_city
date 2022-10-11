import numpy as np
import matplotlib.pyplot as plt
array_1 = np.arange(5,16)
print("Array ranging from 5-15 - ",array_1)
array_2 = np.arange(3,23,3)
print("Array containing 7 evenly spaced numbers between 0 and 23 - ",array_2)
array_3 = np.linspace(-1, 1, 10)
print("Array of evenly distributed values between -1 and 1 - ",array_3)

counts, bins = np.histogram(array_2)
plt.hist(bins[:-1], bins, weights=counts)

random_array_1 = np.random.random_integers(1,100,10)
random_array_2 = np.random.random_integers(1,100,10)
print(random_array_1)
print(random_array_2)
final_array=[]
for i in range(0,len(random_array_1)):
    final_array.append(np.sqrt((random_array_1[i]-random_array_2[i])**2))
print("Euclidean Distance of two random arrrays - ",final_array)