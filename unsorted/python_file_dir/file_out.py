import os
import subprocess,time,io
import sys

cmd = ['python','-c',r"""\
import sys, time, datetime
for i in range(4):
    nl = '\n' if i else ''
    sys.stdout.write(f'{nl}{datetime.datetime.now()} line {i = }')
    sys.stdout.flush()
    time.sleep(0.5)
"""]

file = open('out','ab')
proc = subprocess.Popen(cmd,stdout=file)

# proc = subprocess.Popen(cmd,stdout=subprocess.PIPE)
# for line in proc.stdout:
#     print(f'READ: {line=}')