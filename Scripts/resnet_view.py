import re

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
        comm_time_list.append(sum([float(round_matches[i*seconds_size+j]) for j in range(3)]))
        cpu_time_list.append(float(seconds_matches[i*seconds_size+3]))
        
    return comm_list, round_list, comm_time_list, cpu_time_list
    
models = ['resnet18_infra_wan_', 'resnet50_infra_wan_']

for model in models:
    for i in range(1, 5):
        model_path = model + str(i)
        print(model_path)
        try:
            comm_list, round_list, comm_time_list, cpu_time_list = loaddata(model_path)
            print('comm:', comm_list)
            print('round:', round_list)
            print('comm_time:', comm_time_list)
            print('cpu_time:', cpu_time_list)
            print()
        except:
            pass

