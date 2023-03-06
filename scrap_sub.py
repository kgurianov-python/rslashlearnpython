from subprocess import Popen, PIPE, STDOUT
import re

p = Popen(["ping", "-t", "google.com"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
for line in p.stdout:
    print(line)
    match = re.search(r'\btime=(.*) ',line.decode())
    if match:
        print(match.groups()[0])