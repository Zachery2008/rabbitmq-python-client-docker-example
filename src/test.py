import subprocess

process = subprocess.Popen(['az', 'account', 'list', '--verbose'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
out, err = process.communicate()
print(out)
print(err)