import re

f = open("regex_sum_300111.txt","r")

total = 0
count = 0
for line in f.readlines():
    if not re.search('[0-9]+',line): continue
    num = re.findall('([0-9]+)',line)
    for n in num:
        count += 1
        total += int(n)
print(total,count)