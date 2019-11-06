import os
import time
import subprocess
import sys

fileList = []
#rootdir = input("Root Dir: ")
rootdir = "queue/"
FILENAME = os.getenv('FILENAME')

runstr = '"HandBrakeCLI" -i "{0}" -o "{1}" --preset-import-file "HQ 1080p30 Surround.json" -Z "My HQ Surround"'

inFile = rootdir+FILENAME
pathname, noPath = os.path.split(inFile)
fileName, fileExtension = os.path.splitext(noPath)
outFile = 'output/'+fileName+'.mp4'
movedFile = 'processed/'+inFile

print('Processing %s to %s' % (inFile,outFile))
returncode  = subprocess.run(runstr.format(inFile,outFile), shell=True)
print('RetrunCode: %s' % returncode)
time.sleep(5)
print('Moving',inFile)
os.rename(inFile,movedFile)
