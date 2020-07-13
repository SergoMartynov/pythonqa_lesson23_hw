import subprocess

args = ['uname', '--kernel-release']
kernel_version = subprocess.check_output(args)
print(kernel_version)
