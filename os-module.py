import os
from datetime import datetime

# print(dir(os))
# explains all of the functions within the module

print(os.getcwd())
os.chdir('/Users/Joey/Desktop')
print(os.getcwd())

# print(os.listdir())

# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1')

# os.removedirs('OS-Demo-2/Sub-Dir-1')

# os.rename('epsxe', 'PS1 Emulator')

print(os.stat('PS1 Emulator').st_size)
print(os.stat('PS1 Emulator').st_mtime)

mod_time=os.stat('PS1 Emulator').st_mtime
print(datetime.fromtimestamp(mod_time))

# for dirpath, dirnames, filenames in os.walk('/Users/Joey/Desktop'):
# 	print('Current Path:', dirpath)
# 	print('Directories:', dirnames)
# 	print('Files:', filenames)
# 	print()

print(os.environ.get('HOME'))

