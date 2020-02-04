# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:16:06 2020

@author: jvan1
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,np.pi/24)
sine_y = np.sin(x)
cos_y = np.cos(x)

plt.plot(x,sine_y,label='Sine')
plt.plot(x,cos_y,label='Cosine')
plt.title('1 Period of Sine and Cosine')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.legend(loc='best')
plt.show()