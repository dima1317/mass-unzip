import os
import sys
import zipfile

if sys.argv[1] == '':
  path = '/'
else:
  path = sys.argv[1]

listOfFiles = os.listdir(path)
for f in listOfFiles:
  with zipfile.ZipFile(path + '/' + f,'r') as zip_f:
    zip_f.extractall(sys.argv[2])
