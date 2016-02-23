def parse(input_file):
    parsed = {}
    with open(input_file, 'r') as open_file:
        text = open_file.read()
        text_split = text.split()
        parsed['num_nodes'] = int(text_split[1])
        parsed['packet_size'] = int(text_split[3])
        r_list = []
        i = 5
        while text_split[i] != 'M':
            r_list.append(int(text_split[i]))
            i += 1
        parsed['random_ranges'] = r_list
        parsed['attempts'] = int(text_split[i + 1])
        parsed['sim_time'] = int(text_split[i + 3].replace(',', ''))
    return parsed
