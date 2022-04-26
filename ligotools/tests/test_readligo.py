#Testing functions in ligotools package
import numpy as np

# LIGO-specific readligo.py imports
from ligotools import readligo as rl
from ligotools import utils as utils


#Test 1: Testing load data L1

def test_data_load_L1():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    
    L1_strain, L1_time, L1_channel_dict = rl.loaddata(fn_L1, 'L1')
    
    assert len(L1_strain) == len(L1_time)
    assert len(L1_channel_dict) != 0
    
#Test 2: Testing load data H1

def test_data_load_H1():
    fn_H1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    
    H1_strain, H1_time, H1_channel_dict = rl.loaddata(fn_H1, 'H1')
    
    assert len(H1_strain) == len(H1_time)
    assert len(H1_channel_dict) != 0
    

#Test 3: Testing reading files    

def test_reading_hdf5_L1():
    filename = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

    assert len(strain) != 0
    assert gpsStart is not None
    assert ts is not None
    assert len(shortnameList) != 0
    assert len(qmask) != 0
    assert len(injmask) != 0
    assert len(injnameList) != 0


#Test 4: Testing reading files

def test_reading_hdf5_H1():
    filename = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain, gpsStart, ts, qmask, shortnameList, injmask, injnameList = rl.read_hdf5(filename)

    assert len(strain) != 0
    assert gpsStart is not None
    assert ts is not None
    assert len(shortnameList) != 0
    assert len(qmask) != 0
    assert len(injmask) != 0
    assert len(injnameList) != 0
    
    