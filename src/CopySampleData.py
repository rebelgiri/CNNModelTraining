# Environment name is sampleTraining

from sys import platform as _platform
import sys
import argparse
import os
import shutil
import tensorflow as tf
from pathlib import Path

if _platform == "linux" or _platform == "linux2":
    SLASH = '/'
else:
    SLASH = '\''

SAMPLE = '_Sample'

RS = 'rs'
SL = 'sl'
SR = 'sr'
FL = 'fl'
FR = 'fr'
STR = 'str'
INNEN = 'innen'
KOMBI = 'kombi'


def main():
    # parameters
    path = args.data_dir  # Directory path where data is saved
    numberOfSample = args.number_of_samples  # number of samples to be copied

    splitStringList = path.split(SLASH)
    folderName = splitStringList[-1]
    sampleDataPath = path.replace(folderName, '')

    if not os.path.isdir(sampleDataPath + folderName + SAMPLE):
        os.mkdir(sampleDataPath + folderName + SAMPLE)
        print("Successfully created the directory %s " % path)

    dirList = os.listdir(path)
    for labelFolder in dirList:
        if labelFolder == STR or labelFolder == INNEN or \
                labelFolder == FL or labelFolder == FR or \
                labelFolder == KOMBI or labelFolder == RS or \
                labelFolder == SL or labelFolder == SR:
            labeledImages = os.listdir(path + SLASH + labelFolder)
            count = 0
            for file in labeledImages:
                if count < numberOfSample:
                    if not os.path.isdir(sampleDataPath + folderName + SAMPLE + SLASH + labelFolder):
                        os.mkdir(sampleDataPath + folderName + SAMPLE + SLASH + labelFolder)

                    print(path + SLASH + labelFolder + SLASH + file)
                    shutil.copy(path + SLASH + labelFolder + SLASH + file,
                                    sampleDataPath + folderName + SAMPLE + SLASH + labelFolder)
                    count = count + 1

                    if count == numberOfSample:
                        break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir',
                        type=str,
                        default='',
                        help='Provides path of data.')
    parser.add_argument('--number_of_samples',
                        type=int,
                        default=100,
                        help='Provides number of sample data has to be taken for sample training.')

    args = parser.parse_args()
    main()
