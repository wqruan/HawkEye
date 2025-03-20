import re
import numpy as np

frameworks = ['original', 'taso', 'hawkeye']

def loaddata(path):
    with open(path, 'r') as file:
        data = file.read()

    mb_pattern = r'(\d+\.\d+)\sMB'
    round_pattern = r'(\d+)\srounds'
    seconds_pattern = r'(\d+\.\d+)\sseconds'

    mb_matches = re.findall(mb_pattern, data)
    round_matches = re.findall(round_pattern, data)
    seconds_matches = re.findall(seconds_pattern, data)
    mb_size = len(mb_matches) // 3
    round_size = len(round_matches) // 3
    seconds_size = len(seconds_matches) // 3
    
    # print(mb_matches)
    # print(round_matches)
    # print(seconds_matches)

    comm_list = []
    round_list = []
    comm_time_list = []
    cpu_time_list = []
    for i in range(0, 3):
        comm_list.append(float(mb_matches[i*mb_size+4]))
        round_list.append(int(round_matches[i*round_size+3]))
        comm_time_list.append(sum([float(seconds_matches[i*seconds_size+j]) for j in range(3)]))
        cpu_time_list.append(float(seconds_matches[i*seconds_size+3]))
        
    return comm_list, round_list, comm_time_list, cpu_time_list
    
models = ['resnet18_infra_wan_', 'resnet50_infra_wan_']

for model in models:
    comm_table = []
    round_table = []
    comm_time_table = []
    cpu_time_table = []
    for i in range(1, 5):
        model_path = model + str(i)
        # print(model_path)
        try:
            comm_list, round_list, comm_time_list, cpu_time_list = loaddata(model_path)
            comm_table.append(comm_list)
            round_table.append(round_list)
            comm_time_table.append(comm_time_list)
            cpu_time_table.append(cpu_time_list)
        except:
            pass
    comm_table = np.array(comm_table)
    round_table = np.array(round_table)
    comm_time_table = np.array(comm_time_table)
    cpu_time_table = np.array(cpu_time_table)

    for i in range(3):
        print(model + frameworks[i])
        print('comm: {} MB'.format(np.mean(comm_table[:,i])))
        print('round:', np.mean(round_table[:,i]))
        print('comm_time: {} ({}) seconds'.format(np.mean(comm_time_table[:,i]), np.std(comm_time_table[:,i])))
        print()

