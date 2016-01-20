# Author: Blake Azuela
# Date - Jan 18, 2016
#
# This script is intended to be used to parse a Barracuda VR project
# directory to determine the executable/installation deployment name.
# This is done by locating and parsing the main.cpp file to determine
# version.
#
# COPYRIGHT CPFD SOFTWARE, LLC, 1998-2015. ALL RIGHTS RESERVED
# All information is proprietary and confidental to Arena-flow, LLC

# looking for the following
# define VER_NUM    "17.0.4.i013"
# define BUILD_DATE "Fri Jan 15 14:12:49 MST 2016"
# define RELEASE_NUM "17.0.4"
# define INP_NUM      1701

# Imports
import os.path

# Global Constants
VER_NUM = '#define VER_NUM'
RELEASE_NUM = '#define RELEASE_NUM'

# Data Variables
versionNumber = ''
releaseNumber = ''

# Begin
mainFilePath = "S:\\alex_lucero\\temp_ba_location\\trunk\\barracuda\\main.cpp"
# Ensure main.cpp is found
if os.path.isfile(mainFilePath):
    mainFile = open(mainFilePath)
else:
    print("ERROR: Unable to locate main.cpp file for parsing.")
    exit()
# Open file and extract text lines to string list
mainFileTextList = mainFile.readlines()
for textListIndex in range(len(mainFileTextList)):
    if mainFileTextList[textListIndex].startswith(VER_NUM):
        versionNumber = mainFileTextList[textListIndex]
    if mainFileTextList[textListIndex].startswith(RELEASE_NUM):
        releaseNumber = mainFileTextList[textListIndex]
    if not versionNumber == '' and not releaseNumber == '':
        break

# Remove any surrounding spaces
versionNumber = versionNumber.strip()
releaseNumber = releaseNumber.strip()

# PROFIT!
versionNumber = versionNumber[(versionNumber.find('"')+1):len(versionNumber)-1]
releaseNumber = releaseNumber[(releaseNumber.find('"')+1):len(releaseNumber)-1]

print(versionNumber)
print(releaseNumber)
