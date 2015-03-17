import numpy as np
import matplotlib.pyplot as plt
import getopt
import sys
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
        pts.append([ptBottomX, ptBottomY])

        basicTopY = trY;
        ptTopX = np.random.normal(i, intervalVar)
        ptTopY = basicTopY + np.random.normal(0, noiseVar)
        pts.append([ptTopX, ptTopY])

        i = ((ptBottomX + ptTopX) / 2) + basicInterval

    i = blY;
    while (i < trY):
        basicBottomX = blX;
        ptBottomX = basicBottomX + np.random.normal(0, noiseVar)
        ptBottomY = np.random.normal(i, intervalVar)

        pts.append([ptBottomX, ptBottomY])

        basicTopX = trX;
        ptTopX = basicTopX + np.random.normal(0, noiseVar)
        ptTopY = np.random.normal(i, intervalVar)
        pts.append([ptTopX, ptTopY])

        i = ((ptBottomY + ptTopY) / 2) + basicInterval


    return pts




def main():
    count = 10
    basicInterval = 0.01
    intervalVar = 0.005
    noiseVar = 0.01

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hc:n:i:d:', ['help', 'example-count=', 'noise-variance=', 'basic-interval=', 'interval-variance='])
    except getopt.GetoptError:
        print 'generator.py -c <example-count> -n <noise-variance> -i <basic-interval> -d <interval-variance>'
        print 'Points are generated thusly: every basic-interval along all sides of the square, we shift along the line by x ~ N(0, interval-variance) and perpendicular to the line by y ~ N(0, noise-variance), and place a point'
        return 1

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'generator.py -c <exampleCount> -n <noise> -d <density>'
            print 'Points are generated thusly: every basic-interval along all sides of the square, we shift along the line by x ~ N(0, interval-variance) and perpendicular to the line by y ~ N(0, noise-variance), and place a point'
            return 1
        elif opt in ('-c', '--example-count'):
            count = int(arg)
        elif opt in ('-n', '--noise-variance'):
            noiseVar = float(arg)
        elif opt in ('-i', '--basic-interval'):
            basicInterval = float(arg)
        elif opt in ('-d', '--interval-variance'):
            intervalVar = float(arg)

    for i in range(count):
        pts = generateSquare(noiseVar=noiseVar, basicInterval=basicInterval, intervalVar=intervalVar)
        print pts



if __name__ == "__main__":
    sys.exit(main())
