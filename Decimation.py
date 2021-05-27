import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# decimation using without any predefined fucntion
def sig_deci_1(sample11,sample12):
    x1 = np.linspace(-10, 10, sample11, endpoint=False)
    y1 = np.cos(-x1**2/6.0) + np.sin(-x1**2/6.0)
    xnew1 = np.linspace(-10, 10, sample12, endpoint=False)
    ynew1 = np.cos(-xnew1**2/6.0) + np.sin(-xnew1**2/6.0)
    plt.plot(x1, y1, xnew1, ynew1, 10, y1[0], 'ro')
    plt.legend(['data', 'decimated'], loc='best')
    plt.title("Signal and Sampling")
    plt.xlabel("Time(Unit)")
    plt.ylabel("Amplitude(Unit)")
    plt.show()
    
sig_deci_1(200000,10)

# decimation using "resamlpe" fucntion
def sig_deci_2(sample21,sample22):
    x2 = np.linspace(-10, 10, sample21, endpoint=False)
    y2 = np.cos(-x2**2/6.0) + np.sin(-x2**2/6.0)
    f2 = signal.resample(y2, sample22)
    xnew2 = np.linspace(-10, 10, sample22, endpoint=False)
    plt.plot(x2, y2, xnew2, f2, 10, y2[0], 'ro')
    plt.legend(['data', 'decimated'], loc='best')
    plt.title("Signal and Sampling")
    plt.xlabel("Time(Unit)")
    plt.ylabel("Amplitude(Unit)")
    plt.show()
    
sig_deci_2(200000,10)  


