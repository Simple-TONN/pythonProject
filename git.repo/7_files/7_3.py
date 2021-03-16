from pprint import pprint

file_list = ['1.txt', '2.txt', '3.txt']
text_info = []
data_lines = ''

for each_file in file_list:
    file = open(each_file, encoding='UTF-8')
    data_lines = file.read().splitlines()
    text_info.append([len(data_lines), data_lines, each_file])
    file.close()
text_info.sort()


with open('result.txt', 'w') as file:
    for each_text in text_info:
        file.write(str(each_text[2]) + '\n')
        file.write(str(each_text[0]) + '\n')
        for each_line in each_text[1]:
            file.write(each_line + '\n')
