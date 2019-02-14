import os

for dir, subdir, file in os.walk('C:\\Users\\ehatagu\\PycharmProjects'):
    print('Pycharm Folder', dir)

    for subdirs in subdir:
        print('Pycharm dir:',dir,'subdir:',subdirs)

    for files in file:
        if files.endswith('.py'):
            print('Pycharm dir:',dir,'filename:',files)