import subprocess

current_dir = subprocess.call('pwd', shell=True)
files_into_dir = subprocess.call('ls', shell=True)
print(current_dir)
print(files_into_dir)
