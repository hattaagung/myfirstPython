import re

f = open("mbox-short.txt","r")

for line in f.readlines():
    line = line.strip()
    if re.search("^From: ", line):
        print(line)