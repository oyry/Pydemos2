import requests
from datadriver import reader,wirter
def run(line):
    if line[3]=='post':
        requests.post(line[4],line[5])
        return
reader.open_excel('')
wirter.copy_open('')
reader.readline()
for i in range(1,reader.r):
    line=reader.readline()
    print(line)
    if len(line[0]>2 or line[1]>2):
        pass
    else:
        run(line)
wirter.save_close()