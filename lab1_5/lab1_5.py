import glob
list_files = glob.glob("C:/Users/ds.kiselev/PycharmProjects/*.log")
list_of_ip_add = []
for file in list_files:
    with open(file, 'r') as f:
        for lines in f:
            if 'ip address' in lines and 'no' not in lines:
                list_of_ip_add.append(lines.replace('\n', '')[1::])
print(set(list_of_ip_add))



