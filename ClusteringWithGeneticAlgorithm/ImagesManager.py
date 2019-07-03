import os as operationSystem
from builtins import print
import cv2 as imageReader
import numpy as np


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


def getAllFeaturesMean(features):
    sumFeatures = 0
    for feature in features:
        sumFeatures += feature
    return sumFeatures / len(features)


def getDissimilarityMatrix(allPpmImagesFeatures):
    dissimilarityMatrix = []
    for lineIndex in range(0, len(allPpmImagesFeatures)):
        dissimilarityLine = []
        for columnIndex in range(0, len(allPpmImagesFeatures)):
            differenceVector = []
            imageMean = getAllFeaturesMean(allPpmImagesFeatures[lineIndex])
            differenceVector.append(imageMean)
            imageMeanToCompare = getAllFeaturesMean(allPpmImagesFeatures[columnIndex])
            differenceVector.append(imageMeanToCompare)
            dissimilarityLine.append(np.std(differenceVector))
        dissimilarityMatrix.append(dissimilarityLine)
    return dissimilarityMatrix

def getDissimilarityMatrixImagesForClustering(imageLimiter, rootPath):
    # ppmImage2 = imageReader.imread('Images/Images3/images(2).jpg')
    # ppmImage3 = imageReader.imread('Images/Images3/images(3)')
    # ppmImage4 = imageReader.imread('Images/Images2/images(3)')
    # ppmImage5 = imageReader.imread('Images/Images4/images(3)')

    contImage = 0
    allPpmImages = loadAllImagesInPpmByDirectory(rootPath)
    allImagesFeatures = []
    for ppmImage in allPpmImages:
        imageFeature = []
        if (contImage == imageLimiter):
            break
        imageFeature.append(getDensityRedInImage(ppmImage))
        imageFeature.append(getDensityGreenInImage(ppmImage))
        imageFeature.append(getDensityBlueInImage(ppmImage))
        imageFeature.append(getImagePercentageDensityUsingVerticalFilter(ppmImage))
        imageFeature.append(getImagePercentageDensityUsingHorizontalFilter(ppmImage))
        allImagesFeatures.append(imageFeature)
        contImage = contImage + 1
    return getDissimilarityMatrix(allImagesFeatures)

print(np.matrix(getImagesForClustering(3, 'Images')))
# print('Percentage Using Vertical Filter: ', getImagePercentageDensityUsingVerticalFilter(ppmImage))
# print('Percentage Using Horizontal Filter: ', getImagePercentageDensityUsingHorizontalFilter(ppmImage))
# print('Red density: ', getDensityRedInImage(ppmImage))
# print('Green density: ', getDensityGreenInImage(ppmImage))
# print('Blue density: ', getDensityBlueInImage(ppmImage))