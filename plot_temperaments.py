'''
Plotting the temperaments
'''
from temperament import *
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 12, 1)

werck_iii_fifth = fifth_tempering_for(WERCK_III)(x)
werck_iv_fifth = fifth_tempering_for(WERCK_IV)(x)
meantone_fifth = fifth_tempering_for(MEANTONE)(x)
et_fifth = fifth_tempering_for(EQUAL_TEMPERAMENT)(x)
acs_i_fifth = fifth_tempering_for(ACS_I)(x)
acs_ii_fifth = fifth_tempering_for(ACS_II)(x)

werck_iii_third = third_tempering_for(WERCK_III)(x)
werck_iv_third = third_tempering_for(WERCK_IV)(x)
meantone_third = third_tempering_for(MEANTONE)(x)
et_third = third_tempering_for(EQUAL_TEMPERAMENT)(x)
acs_i_third = third_tempering_for(ACS_I)(x)
acs_ii_third = third_tempering_for(ACS_II)(x)

plt.axis([0, 40, 0, 30])
plt.plot(werck_iii_fifth.max(), werck_iii_third.std(), 'r-<',
        werck_iv_fifth.max(), werck_iv_third.std(), 'g->', 
        meantone_fifth.max(), meantone_third.std(), 'b-o', 
        et_fifth.max(), et_third.std(), 'k-x',
        acs_i_fifth.max(), acs_i_third.std(), 'y-d', 
        acs_ii_fifth.max(), acs_ii_third.std(), 'c-D')

# Set the axes markers
plt.legend(['Werckmeister III', 'Werckmeister IV', 'Meantone', 'Equal Temperament', 'ACS I', 'ACS II'])

# Labels
plt.xlabel('Worst tempering of fifth', fontsize=14, color='black')
plt.ylabel('Standard deviation of error in thirds', fontsize=14, color='black')

plt.show()
# plt.savefig(__file__ + '.png')

