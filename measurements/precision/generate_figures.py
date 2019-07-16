from parse import read_data
import numpy as np
import matplotlib.pyplot as plt
import os

def calculate_statistics(data):
    mean = np.mean(data)
    var = np.var(data, ddof=1)
    sigma = var**(1/2)
    return [mean, var, sigma]

def save_histogram(data, name):
    mean, var, sigma = calculate_statistics(data)
    fig, ax = plt.subplots()
    ax.hist(data, bins=100)
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    text = "Mean: {:<1.2f}\n".format(mean) +\
           "Sigma: {:<1.2f}\n".format(sigma)
    ax.text(0.80, 0.95, text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    plt.xlabel('ns')
    plt.savefig('/home/milosz/Projects/master/figures/measurements/' +
                name + '.svg', format='svg')

meas_path = '/home/milosz/Projects/master/measurements/precision/'
save_path = '/home/milosz/Projects/master/figures/measurements/'

#for file in os.listdir(meas_path):
#    if file.endswith('.txt'):
#        data = read_data(meas_path + file)
#        save_histogram(data, file.replace('.txt', ''))
file = 'WRTD_other_day.txt'
data = read_data(meas_path + file)
save_histogram(data, file.replace('.txt', ''))

