# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:01:01 2020

@author: Owner
"""


import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
from scipy.interpolate import interp1d
import pandas as pd

'''
downsample to match with the dataset
'''
def downsample(array, npts):
    interpolated = interp1d(np.arange(len(array)), array, axis = 0, fill_value = 'extrapolate')
    downsampled = interpolated(np.linspace(0, len(array), npts))
    return downsampled


#get all the file names of the given directory
path='C:/Android/platform-tools_r30.0.4-windows/platform-tools/mydata/data/'
files = [path+f for f in listdir(path) if isfile(join(path, f))]
files.sort()

downsampled_data={'ts':[],'gesture': [], 'x': [],'y':[],'z':[]}

for i,file in enumerate(files):
    gesture=int(i/10)+1
    
    f = open(file, "r")
    lines=f.readlines()
    lines=lines[1:]
    f.close()


    data = {'ts': [], 'x': [],'y':[],'z':[]}
    for line in lines:
        splt=line.split(',')
        ts,x,y,z=int(splt[0]),float(splt[3]),float(splt[4]),float(splt[5][0:-1])
        data['ts'].append(ts)
        data['x'].append(x)
        data['y'].append(y)
        data['z'].append(z)    
        
    
    
    #average sampling rate in Hz (timestamps are in ms)
    sampling_rate=len(data['ts'])/(data['ts'][-1]-data['ts'][0])*1000
    required_sample_rate=9.1
    #downsample this at 9.1Hz
    required_samples=int(len(data['ts'])*required_sample_rate/sampling_rate)
    
    downsampled_ts = downsample(data['ts'], required_samples)
    downsampled_x = downsample(data['x'], required_samples)
    downsampled_y = downsample(data['y'], required_samples)
    downsampled_z = downsample(data['z'], required_samples)
    
    downsampled_data['ts'].append(downsampled_ts)
    downsampled_data['gesture'].append(gesture)
    downsampled_data['x'].append(downsampled_x)
    downsampled_data['y'].append(downsampled_y)
    downsampled_data['z'].append(downsampled_z)


data=pd.DataFrame(downsampled_data)
data.to_pickle('C:/Users/Owner/code/smartwatch/project/mydata.pkl')
pd.read_pickle('C:/Users/Owner/code/smartwatch/project/mydata.pkl')

    
    
    
    
    
    
    
    
    
    
    