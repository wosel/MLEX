import numpy as np

import getopt
import sys
import math

"""
send to rkrivak@gmail.com
"""

def generateSquare(basicInterval=0.01, intervalVar=0.005, noiseVar=0.01):
    blX = 0.1
    blY = 0.1

    trX = 0.9
    trY = 0.9

    pts = []
    i = blX;

    #generate top and bottom line
    while (i < trX):
        basicBottomY = blY;
        ptBottomX = np.random.normal(i, intervalVar)
        ptBottomY = basicBottomY + np.random.normal(0, noiseVar)
        if ptBottomX > 1.: ptBottomX = 1.
        if ptBottomX < 0.: ptBottomX = 0.
        if ptBottomY > 1.: ptBottomY = 1.
        if ptBottomY < 0.: ptBottomY = 0.
        pts.append([ptBottomX, ptBottomY])

        basicTopY = trY;
        ptTopX = np.random.normal(i, intervalVar)
        ptTopY = basicTopY + np.random.normal(0, noiseVar)
        if ptTopX > 1.: ptTopX = 1.
        if ptTopX < 0.: ptTopX = 0.
        if ptTopY > 1.: ptTopY = 1.
        if ptTopY < 0.: ptTopY = 0.
        
        pts.append([ptTopX, ptTopY])

        i = ((ptBottomX + ptTopX) / 2) + basicInterval

    i = blY;
    while (i < trY):
        basicBottomX = blX;
        ptBottomX = basicBottomX + np.random.normal(0, noiseVar)
        ptBottomY = np.random.normal(i, intervalVar)
        if ptBottomX > 1.: ptBottomX = 1.
        if ptBottomX < 0.: ptBottomX = 0.
        if ptBottomY > 1.: ptBottomY = 1.
        if ptBottomY < 0.: ptBottomY = 0.

        pts.append([ptBottomX, ptBottomY])

        basicTopX = trX;
        ptTopX = basicTopX + np.random.normal(0, noiseVar)
        ptTopY = np.random.normal(i, intervalVar)
        if ptTopX > 1.: ptTopX = 1.
        if ptTopX < 0.: ptTopX = 0.
        if ptTopY > 1.: ptTopY = 1.
        if ptTopY < 0.: ptTopY = 0.
        pts.append([ptTopX, ptTopY])

        i = ((ptBottomY + ptTopY) / 2) + basicInterval


    return pts

def getPts(intervalLog, noiseLog):
    biLog = np.random.normal(intervalLog, 0.5)
    nLog = np.random.normal(noiseLog, 0.5)

    if biLog > -1: biLog = -1
    if biLog < -3: biLog = -3
    bi = math.pow(10, biLog)
    n = math.pow(10, nLog)
    iv = bi/2.

    return generateSquare(noiseVar=n, basicInterval=bi, intervalVar=iv)



def main():
    count = 10
    basicInterval = 0.01
    noiseVar = 0.01

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:n:i:d:', ['help', 'example-count=', 'noise-variance='])
    except getopt.GetoptError:
        print 'generator.py -c <example-count> -n <noise-variance> -i <basic-interval> -d <interval-variance>'
        print 'Points are generated thusly: every basic-interval along all sides of the square, we shift along the line by x ~ N(0, basic-interval/2) and perpendicular to the line by y ~ N(0, noise-variance), and place a point'
        return 1

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'generator.py -c <exampleCount> -n <noise> -d <density>'
            print 'Points are generated thusly: every basic-interval along all sides of the square, we shift along the line by N(0, basic-interval/2) and perpendicular to the line by y ~ N(0, noise-variance), and place a point'
            return 1
        elif opt in ('-c', '--example-count'):
            count = int(arg)
        elif opt in ('-n', '--noise-variance'):
            noiseVar = float(arg)
        elif opt in ('-i', '--basic-interval'):
            basicInterval = float(arg)



    intervalLog = math.log(basicInterval, 10)
    noiseLog = math.log(noiseVar, 10)

    for i in range(count):

        pts = getPts(intervalLog, noiseLog)
        while (len(pts) < 10) or (len(pts) > 1000):

            pts = getPts(intervalLog, noiseLog)
        print pts


if __name__ == "__main__":
    sys.exit(main())
