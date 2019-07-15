import matplotlib.pyplot as plt
import numpy as np
from parse import read_data


plt.rcParams["font.family"] = "serif"

def add_data_to_fig(data, label, xlabel, ylabel):
    #plt.plot(data['postsamples'], data['medium'], label=label)
    #plt.semilogx(data['postsamples'], data['medium'], label=label)
    plt.subplot(211)
    plt.errorbar((data['postsamples']), data['medium'],
                 yerr=data['std_dev'], label=label)
    plt.legend(loc='best')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.subplot(212)
    plt.errorbar((data['postsamples']), data['medium'],
                 yerr=data['std_dev'], label=label)
    plt.xscale('log')
    plt.legend(loc='best')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout(pad=0)


meas_path = '/home/milosz/Projects/master/measurements/freq_meas/'
save_path = '/home/milosz/Projects/master/figures/measurements/'

file_name = meas_path + 'loop_adc/frequency_meas.txt'
loop_adc = read_data(file_name)[3]

file_name = meas_path + 'loop_server/frequency_meas.txt'
loop_server = read_data(file_name)[3]





add_data_to_fig(loop_adc, 'ADC loop', 'postsamples',
                'acquisition frequency[Hz]')
add_data_to_fig(loop_server, 'Server loop', 'postsamples',
                'acquisition frequency[Hz]')
plt.savefig(save_path + 'loop_adc_server_comparison.svg', format='svg')

