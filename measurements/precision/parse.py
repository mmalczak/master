def read_data(file_name):
    d = None
    with open(file_name, 'r') as f:
        d = f.readlines()
    data_all = [] 
    for i in d:
        if i.startswith('Data: ['):
            i = i.replace('Data: [', '')
            i = i.replace(']', '')
            data = i.split(',')
            data = [float(value) for value in data]
            return data

