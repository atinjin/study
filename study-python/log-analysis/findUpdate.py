
f = open("available2.log")

while True:
    line = f.readline()
    line = line.strip()
    length = len(line)
    if( line[length-1:length] != '0'):
        print(line)
    if not line: break

f.close()