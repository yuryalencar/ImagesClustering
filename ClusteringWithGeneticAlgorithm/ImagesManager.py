import os as operationSystem
from builtins import print
import cv2 as imageReader

def loadAllImagesInPpmByDirectory(imagesRootPath):
    foldersImages = operationSystem.listdir(imagesRootPath)
    allImages = []
    for folder in foldersImages:
        pathJoined = operationSystem.path.join(imagesRootPath, folder)
        allFileIntoFolder = operationSystem.listdir(pathJoined)
        for nameImage in allFileIntoFolder:
            pathJoined = operationSystem.path.join(imagesRootPath, folder, nameImage)
            ppmImage = imageReader.imread(pathJoined)
            allImages.append(ppmImage)
    return allImages


def getImagePercentageDensityUsingVerticalFilter(ppmImage):
    verticalFilter = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    return getImagePercentageDensityUsingFilter(verticalFilter, ppmImage)


def getImagePercentageDensityUsingHorizontalFilter(ppmImage):
    horizontalFilter = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
    return getImagePercentageDensityUsingFilter(horizontalFilter, ppmImage)

def getImagePercentageDensityUsingFilter(filter, ppmImage):
    amountLines = len(ppmImage)
    amountColumns = len(ppmImage[0])
    imageAfterFilter = [[[0]] * amountColumns] * amountLines

    sumToFilterResult = 0
    for lineNumber in range(1, len(ppmImage) - 1):
        for columnNumber in range(1, len(ppmImage[lineNumber]) - 1):
            filterResult = 0
            for centralizeLine in range(-1, 2):
                for centralizeColumn in range(-1, 2):
                    filterResult += int(filter[centralizeLine + 1][centralizeColumn + 1] *
                                        ppmImage[lineNumber + centralizeLine][columnNumber + centralizeColumn][0])
            imageAfterFilter[lineNumber][columnNumber] = abs(filterResult)
            sumToFilterResult += abs(filterResult)

    amountPixels = amountLines * amountColumns
    percentageDensity = sumToFilterResult / amountPixels
    return percentageDensity

def getDensityRedInImage(ppmImage):
    return getDensityColorInImage(ppmImage, 0)

def getDensityGreenInImage(ppmImage):
    return getDensityColorInImage(ppmImage, 1)

def getDensityBlueInImage(ppmImage):
    return getDensityColorInImage(ppmImage, 2)

def getDensityColorInImage(ppmImage, positionRgb):
    amountLines = len(ppmImage)
    amountColumns = len(ppmImage[0])

    sumAmountColorInImage = 0
    for lineNumber in range(1, len(ppmImage) - 1):
        for columnNumber in range(1, len(ppmImage[lineNumber]) - 1):
            sumAmountColorInImage += ppmImage[lineNumber][columnNumber][positionRgb]
    amountPixels = amountLines * amountColumns
    percentageColor = sumAmountColorInImage / amountPixels
    return percentageColor

# allPpmImages = loadAllImagesInPpmByDirectory('Images')
# print(len(allPpmImages))

# OLD ALGORITHM
# res = imageReader.imread('Images/Images3/images(2).jpg')
# pv = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
# # pv = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]  # ph
#
# y = len(res)
# x = len(res[0])
#
# # print(x)
# # print(y)
#
# mp = [[[0]] * x] * y
#
# sum = 0
# with open('out.txt', 'w') as f:
#     for i in range(1, len(res) - 1):
#         for j in range(1, len(res[i]) - 1):
#             acc = 0
#             for k in range(-1, 2):
#                 for o in range(-1, 2):
#                     acc += int(pv[k + 1][o + 1] * res[i + k][j + o][0])
#                     # print(acc)
#
#             mp[i][j] = abs(acc)
#             sum += abs(acc)
#
#             print(mp[i][j], file=f)
#
# r = ((y - 1) * (x - 1))
# result = sum / r
# print(result)

# allPpmImages = loadAllImagesInPpmByDirectory('Images')
ppmImage = imageReader.imread('Images/Images3/images(2).jpg')
print('Percentage Using Vertical Filter: ', getImagePercentageDensityUsingVerticalFilter(ppmImage))
print('Percentage Using Horizontal Filter: ', getImagePercentageDensityUsingHorizontalFilter(ppmImage))
print('Red density: ', getDensityRedInImage(ppmImage))
print('Green density: ', getDensityGreenInImage(ppmImage))
print('Blue density: ', getDensityBlueInImage(ppmImage))

