import subprocess

pid_info = subprocess.call('pgrep telegram', shell=True)
print(pid_info)
