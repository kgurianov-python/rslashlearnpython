import os
import time
import datetime


#
def follow(thefile):
    '''generator function that yields new lines in a file
    '''
    # seek the end of the file
    thefile.seek(0, os.SEEK_END)

    # start infinite loop
    while True:
        # read last line of file
        line = thefile.readline()
        # sleep if file hasn't been updated
        if not line.strip():
            time.sleep(0.1)
            continue

        yield line



# input = open('out', "rb")
# loglines = follow(input)
#
# for line in loglines:
#     print(f"{line=}")

with open('out', "rb") as fp:
    lines = []
    while True:
        line = fp.readline()
        if not line:
            time.sleep(0.01)
            continue
        lines.append(line)
        if b'\n' in line:
            line = b'\r'.join(lines)
            lines = []
            print(f'READ: {line = }',flush=True)
    if lines: # Final still not \n terminated
        line = b'\r'.join(lines)
        print(f'READ: {line = }',flush=True)

    # proc = subprocess.Popen(cmd,stdout=subprocess.PIPE)
# for line in proc.stdout:
#     print(f'READ: {line=}')