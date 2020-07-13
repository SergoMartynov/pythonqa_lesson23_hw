from subprocess import Popen

args = ["ps", "-ef"]
all_processes = Popen(args)
print(all_processes)
