'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''
input_name = input('请输入文件名：')
index = input_name.rfind('.')
copy_name = input_name[:index] + '_bak' + input_name[index:]
print(copy_name)
input_file = open(input_name)
copy_file = open(copy_name,'w')

line = input_file.readline()
while line:
    copy_file.write(line)
    line = input_file.readline()

input_file.close()
copy_file.close()

filename = input('请输入要统计的文件名：')
f = open(filename,encoding='utf-8')
empty_count = 0
command_count = 0
code_count = 0

line = f.readline()
while line:
    if not line.strip():
        empty_count += 1
    elif line.strip().startswith('#'):
        command_count += 1
    else:
        code_count += 1

    line = f.readline()

print('代码数：%d，空行数：%d，注释数：%d'%(code_count,empty_count,command_count))
f.close()