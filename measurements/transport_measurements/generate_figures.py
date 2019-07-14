import matplotlib.pyplot as plt
import numpy as np
from parse import read_data


plt.rcParams["font.family"] = "serif"

def add_data_to_fig(data, label):
    plt.plot(data['postsamples'], data['medium'], label=label)
    #plt.semilogx(data['postsamples'], data['medium'], label=label)
    #plt.errorbar(data['postsamples'], data['medium'],
    #             yerr=data['std_dev'], fmt='-o', label='bleble')
    plt.legend(loc='best')

meas_path = '/home/milosz/Projects/master/measurements/transport_measurements/'
save_path = '/home/milosz/Projects/master/figures/measurements/'

file_name = meas_path + 'XMLRPC/XMLRPC_efficiency_ZMQRPC.txt'
XML_dat_4_chan = read_data(file_name)[3]


file_name = meas_path + 'ZMQ/ZMQ_pickle.txt'
ZMQ_pickle_dat_4_chan = read_data(file_name)[3]

file_name = meas_path + 'numpy/ZMQ/ZMQ_pickle_numpy.txt'
ZMQ_pickle_numpy_dat_4_chan = read_data(file_name)[3]

file_name = meas_path + 'ZMQ/ZMQ_json.txt'
ZMQ_json_dat_4_chan = read_data(file_name)[3]

file_name = meas_path + 'ZMQ/ZMQ_protobuf.txt'
ZMQ_protobuf_dat_4_chan = read_data(file_name)[3]


file_name = meas_path + 'TCP/TCP_pickle.txt'
TCP_pickle_dat_4_chan = read_data(file_name)[3]

file_name = meas_path + 'numpy/TCP/TCP_pickle_numpy.txt'
TCP_pickle_numpy_dat_4_chan = read_data(file_name)[3]

file_name = meas_path + 'TCP/TCP_json.txt'
TCP_json_dat_4_chan = read_data(file_name)[3]

file_name = meas_path + 'TCP/TCP_protobuf.txt'
TCP_protobuf_dat_4_chan = read_data(file_name)[3]




add_data_to_fig(XML_dat_4_chan, 'XMLRPC')
add_data_to_fig(ZMQ_pickle_dat_4_chan, 'ZMQ')
add_data_to_fig(TCP_pickle_dat_4_chan, 'TCP')
plt.xlabel('postsamples')
plt.ylabel('acquisition time [s]')
plt.savefig(save_path + 'xml_zmq_tcp_comparison_pickle.svg', format='svg')

plt.clf()
add_data_to_fig(ZMQ_pickle_dat_4_chan, 'ZMQ')
add_data_to_fig(TCP_pickle_dat_4_chan, 'TCP')
plt.xlabel('postsamples')
plt.ylabel('acquisition time [s]')
plt.savefig(save_path + 'zmq_tcp_comparison_pickle.svg', format='svg')

plt.clf()
add_data_to_fig(ZMQ_pickle_dat_4_chan, 'pickle')
add_data_to_fig(ZMQ_json_dat_4_chan, 'json')
add_data_to_fig(ZMQ_protobuf_dat_4_chan, 'protobuf')
plt.xlabel('postsamples')
plt.ylabel('acquisition time [s]')
plt.savefig(save_path + 'zmq_serialization_comp.svg', format='svg')

plt.clf()
add_data_to_fig(TCP_pickle_dat_4_chan, 'pickle')
add_data_to_fig(TCP_json_dat_4_chan, 'json')
add_data_to_fig(TCP_protobuf_dat_4_chan, 'protobuf')
plt.xlabel('postsamples')
plt.ylabel('acquisition time [s]')
plt.savefig(save_path + 'tcp_serialization_comp.svg', format='svg')


plt.clf()
add_data_to_fig(ZMQ_pickle_numpy_dat_4_chan, 'ZMQ')
add_data_to_fig(TCP_pickle_numpy_dat_4_chan, 'TCP')
plt.xlabel('postsamples')
plt.ylabel('acquisition time [s]')
plt.savefig(save_path + 'zmq_tcp_comparison_pickle_numpy.svg', format='svg')


