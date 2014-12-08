'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 12, 1)
weights = np.array([0.5, 1.0, 0.5])
weighted_fifth = lambda t: weighted_key_tempering_for(t, weights)

werck_iii = meantone_deviation_for(WERCK_III)(x)
werck_iv = meantone_deviation_for(WERCK_IV)(x)
meantone = meantone_deviation_for(MEANTONE)(x)
et = meantone_deviation_for(EQUAL_TEMPERAMENT)(x)
acs_i = meantone_deviation_for(ACS_I)(x)
acs_ii = meantone_deviation_for(ACS_II)(x)

plt.axis([0, 11, 0, 100])
plt.plot(x, werck_iii, 'r-o', x, werck_iv, 'g-o', x, meantone, 'b-o', x, et, 'k-o', x, acs_i, 'y-o', x, acs_ii, 'c-o')

# Set the axes markers
plt.xticks(x, circle_of_fifths)
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament', 'ACS I', 'ACS II'])

# Labels
plt.xlabel('tonic of key', fontsize=14, color='black')
plt.ylabel('mean tempering of key', fontsize=14, color='black')

plt.show()

