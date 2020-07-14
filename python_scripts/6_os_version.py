import subprocess

args = ['lsb_release', '-d']
os_version = subprocess.check_output(args)
print(os_version)
