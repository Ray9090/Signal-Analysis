import numpy as np
import matplotlib.pyplot as plt

def averaged(x, window_len=10, window='hanning'):

    s=np.r_[2*x[0]-x[window_len:1:-1], x, 2*x[-1]-x[-1:-window_len:-1]]
    #print(len(s))
    
    if window == 'flat': #moving average
        w = np.ones(window_len,'d')
    else:
        w = getattr(np, window)(window_len)
    y = np.convolve(w/w.sum(), s, mode='same')
    return y[window_len-1:-window_len+1]


def averaged_demo():
    t = np.linspace(-20,20,100)
    x = np.cos(-t**2/6.0) + np.sin(-t**2/6.0)
    xn = x + np.random.randn(len(t)) * 0.1
    y = averaged(x)
    ws = 31

    plt.subplot(211)
    plt.plot(np.ones(ws))

    windows=['flat', 'hanning', 'hamming', 'bartlett', 'blackman']

    #plt.hold(True)
    for w in windows[1:]:
        #eval('plt.plot('+w+'(ws) )')
        plt.plot(getattr(np, w)(ws))

    plt.axis([0,30,0,1.1])

    plt.legend(windows)
    plt.title("The smoothing windows")
    plt.subplot(212)
    plt.plot(x)
    plt.plot(xn)
    for w in windows:
        plt.plot(averaged(xn,10,w))
    l = ['original signal', 'signal with noise']
    l.extend(windows)
    plt.legend(l)
    plt.title("Smoothing a noisy signal")
    plt.xlabel("Time(Unit)")
    plt.ylabel("Amplitude(Unit)")
    plt.tight()
    plt.show()


if __name__=='__main__':
    
    # part 1: 1d
    averaged_demo()

    