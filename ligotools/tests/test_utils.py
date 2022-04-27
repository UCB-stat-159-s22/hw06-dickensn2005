
from ligotools import readligo as rl
from ligotools import utils as ut

import numpy as np
import matplotlib.mlab as mlab

from scipy import signal
from scipy.interpolate import interp1d
from scipy.io import wavfile
import os
from os.path import exists
from os import remove
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#Testing the whiten function
def test_whiten():
    fs = 4096
    nfft = 4*4096
    
    fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = nfft)
    psd_H1 = interp1d(freqs, Pxx_H1)

    dt = time_H1[1] - time_H1[0]
    
    strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
    assert type(strain_H1_whiten) == np.ndarray
    assert len(strain_H1_whiten)== len(strain_H1)



#Testing the write_wavfile function
def test_write_wavfile_function():
    data = np.linspace(0,10,100)
    ut.write_wavfile("audio/temp.wav", 1, data)
    assert exists("audio/temp.wav")
    remove("audio/temp.wav")    
    
    
#Testing the reqshift function
def test_reqshift_function():
    fs = 4096
    nfft = 4*4096
    
    fn_H1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = nfft)
    psd_H1 = interp1d(freqs, Pxx_H1)

    dt = time_H1[1] - time_H1[0]
    
    strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
    
    strain_H1_shifting = ut.reqshift(strain_H1,fshift=500,sample_rate=5096)
    assert len(strain_H1_shifting) == len(strain_H1)

#Testing the plotting function
def test_plot_H1_around_event_graphs():
    img = plt.imread('figurs/GW150914_L1_matchfreq.png')
    assert img is not None
   
