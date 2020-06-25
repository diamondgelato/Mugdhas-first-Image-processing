import cv2
import numpy as np

# tried to sort points for warping but then I found a better way

def sortPoints (points):
    topLef, botRig, topRig, botLef = 0, 0, 0, 0
    sumList = []
    diffList = []

    '''
    1st: least sum (easy)
    2nd: higher x
    3rd: higher y
    4th: greatest sum (again, easy)
    '''

    if points.size == 8:
        # minSum, maxSum = points [0, 0, 0] + points [0, 0, 1]

        for index in range(0,4):
            sum = points [index, 0, 0] + points [index, 0, 1]
            diff = points [index, 0, 0] - points [index, 0, 1]

            sumList.append (sum)
            diffList.append (diff)

            '''
            # min sum
            if sum < minSum:
                minSum = sum
                topLef = index

            # max sum
            elif sum > maxSum:
                maxSum = sum
                botRig = index

        for index in range(0,4):
            if index != topLef and index != botRig:
                xCompare.append (index)

        if points [xCompare[0], 0, 0] > points [xCompare[1], 0, 0]:
            topRig = xCompare [0]
            botLef = xCompare [1]
        elif points [xCompare[0], 0, 0] < points [xCompare[1], 0, 0]:
            topRig = xCompare [1]
            botLef = xCompare [0]
        '''


        sortedPoints = np.array ([points [topLef, 0], points [topRig, 0], points [botLef, 0], points [botRig, 0]])
        return sortedPoints

    else:
        pass
