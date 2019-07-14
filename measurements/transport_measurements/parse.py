def read_data(file_name):
    d = None
    with open(file_name, 'r') as f:
        d = f.readlines()
    data_all = [] 
    for i in d:
        if i.startswith('Number'):
            number_of_channels = int(i.split()[3])
            data = {'nb_chan': number_of_channels, 'postsamples': [],
                    'best': [], 'medium': [], 'variance': [], 'std_dev': []}
            data_all.append(data)
        if i.startswith('Postsamples'):
            i = i.replace(',', '')
            a = i.split()
            data['postsamples'].append(int(a[1]))
            data['best'].append(float(a[3]))
            data['medium'].append(float(a[5]))
            data['variance'].append(float(a[7]))
            data['std_dev'].append(float(a[7])**(1/2)) 
    return data_all 



