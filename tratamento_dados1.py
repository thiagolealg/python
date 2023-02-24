import os
# This is the path where you want to search
path = 'C:\\Users\\f9329149\\PycharmProjects\\tudo'

# this is the extension you want to detect
extension = '.csv'

for root, dirs_list, files_list in os.walk(path):
    for file_name in files_list:
        if os.path.splitext(file_name)[-1] == extension:
            file_name_path = os.path.join(root, file_name)
            print(file_name)
            #print(file_name_path)   # This is the full path of the filter file