import matplotlib.pyplot as plt
import numpy as np
from plotting import implot, rtiplot
from time_utils import datetime_to_float

#plotting windows
def plot(mf, r, t, x):
    plt.figure()
    rtiplot(mf, t, r/1e3, title='RX (Matched Filtered)', ylabel='Range (km)', clabel='SNR (dB)', vmin=0, vmax=6)
    plt.tight_layout()
    plt.savefig("plot "+str(x))

def data_plotter(array, r, t, pulse):
    plot(array, r, t, pulse)

"""
def hist1(data, t):
    times = []
    time_length = (t[-1] - t[0])/60
    mins = np.arange(0, time_length)
    for i in range(0, len(data)):
        event_time = (data[i]['t'][0] - t[0])/60
        times.append(event_time)
    plt.hist(times, bins=mins)
    plt.xlabel('Time (Min)')
    plt.ylabel('Num of Hits')
    plt.title('Number of Hits per Minute')
    plt.savefig('hist_hits')
"""

def hist1(data, t0):
    times = []
    for i in range(1, len(data)):
        event_time = (datetime_to_float(data[i]['t'][0]) - t0)/60
        times.append(event_time)
    plt.hist(times, bins=27)
    plt.xlabel('Time (Min)')
    plt.ylabel('Num of Hits')
    plt.title('Number of Hits per Minute')
    plt.savefig('hist_hits')


def hist2(data):
    v_avg = []
    for i in range(1, len(data)):
        v = data['lstsq'][i][1]/1e3
        v_avg.append(v)
    plt.hist(v_avg, bins=np.arange(-70, 10, 5))
    plt.xlabel('Velocity (km/s)')
    plt.ylabel('Num of Objects')
    plt.title('Velocity Distribution')
    plt.savefig('hist_v')

def hist3(data):
    r_avg = []
    for i in range(1, len(data)):
        r = data['lstsq'][i][0]/1e3
        r_avg.append(r)
    plt.hist(r_avg, bins=np.arange(65, 145, 5))
    plt.xlabel('Range (km)')
    plt.ylabel('Num of Objects')
    plt.title('Range Distribution')
    plt.savefig('hist_r')

def hist4(data):
    snr_avg = []
    for i in range(1, len(data)):
        snr = data['snr peak'][i]
        snr_avg.append(snr)
    plt.hist(snr_avg, bins=np.arange(0, 65, 5))
    plt.xlabel('SNR (dB)')
    plt.ylabel('Num of Objects')
    plt.title('SNR Distribution')
    plt.savefig('hist_snr')


   
        
