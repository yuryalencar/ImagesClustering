import random
import numpy as np
import ImagesManager as imageManager


class GeneticAlgorithm:

    def initRandomPopulation(self, amountPopulation, amountClusterings):
        population = [[0 for personCluster in range(amountClusterings)] for personInPopulation in
                      range(amountPopulation)]
        for personInPopulation in range(amountPopulation):
            initRandom = 0
            finalRandom = amountClusterings - 1
            positionCluster = random.randint(initRandom, finalRandom)
            population[personInPopulation][positionCluster] = 1
        return population

    def calculateFitness(self, population, dissimilarityMatrix, amountClusterings):
        populationFitness = []
        for lineIndex in range(0, len(population)):
            sumClusterMembers = 0
            sumMemberFitness = 0
            member = population[lineIndex]
            for clusterPosition in range(amountClusterings):
                if (member[clusterPosition] == 1):
                    sumClusterMembers = sumClusterMembers + 1
                    for columnIndex in range(len(population)):
                        if (population[columnIndex][clusterPosition] == 1):
                            sumClusterMembers = sumClusterMembers + 1
                            sumMemberFitness = sumMemberFitness + (dissimilarityMatrix[lineIndex][columnIndex])
            populationFitness.append(sumMemberFitness/sumClusterMembers * 0.5 * len(population))
        return populationFitness

    def raffleFathersUsingTournament(self, allPopulations, allFitness):
        selectedFathersIndex = []
        selectedFitnessFathers = []
        positionsRaffled = []
        allFathersSorted = False

        while (allFathersSorted == False):
            canSelectFather = True
            initRandom = 0
            finalRandom = len(allPopulations[0])
            selectedPosition = random.randint(initRandom, finalRandom)

            for index in range(len(positionsRaffled)):
                if(positionsRaffled[index] == selectedPosition):
                    canSelectFather = False
                    break
                else:
                    canSelectFather = True

            if(canSelectFather):
                positionsRaffled.append(selectedPosition)
                selectedFathersIndex.append(selectedPosition)
                selectedFitnessFathers.append(allFitness[selectedPosition])

            if(len(selectedFathersIndex) == 3):
                allFathersSorted = True

        betterFatherIndex = 0
        betterFitness = 100000
        for indexFather in range(len(selectedFathersIndex)):
            # print(selectedFitnessFathers[indexFather], selectedFitnessFathers[indexFather] < betterFitness)
            if(selectedFitnessFathers[indexFather] < betterFitness):
                betterFitness = selectedFitnessFathers[indexFather]
                betterFatherIndex = selectedFathersIndex[indexFather]

        return betterFatherIndex

    def fathersCrossover(self, father, mother):
        childs = []
        amountChildGenes = len(father)
        pointForCourt = int(amountChildGenes / 2)

        for indexChild in range(2):
            child = []
            for motherIndex in range(0, pointForCourt):
                if(indexChild == 0):
                    child.append(mother[motherIndex])
                else:
                    child.append(father[motherIndex])
            for fatherIndex in range(pointForCourt - 1, amountChildGenes - 1):
                if (indexChild == 0):
                    child.append(father[fatherIndex])
                else:
                    child.append(mother[fatherIndex])
            childs.append(child)
        return childs

    def childMutation(self, child, percentage):
        initRandom = 0
        finalRandom = 100
        canMutation = random.randint(initRandom, finalRandom)
        if(canMutation < percentage):
            populationLine = random.randint(initRandom, len(child) - 1)
            for indexGene in range(len(child[populationLine])):
                child[populationLine][indexGene] = 0
            genePosition = random.randint(initRandom, len(child[populationLine]) -1)
            child[populationLine][genePosition] = 1
        return child

    def insertChildInPopulationWithElitism(self, allFitness):
        lessFitness = max(allFitness)
        positionLessFitness = allFitness.index(lessFitness)
        return positionLessFitness


dissimilarityMatrix = imageManager.getDissimilarityMatrixImagesForClustering(16, 'Images')
algorithmGenetic = GeneticAlgorithm()
populations = []
populationsFitness = []
numberOfCluster = 4

for populationIndex in range(0, 100):
    population = algorithmGenetic.initRandomPopulation(len(dissimilarityMatrix), numberOfCluster)
    populationFitness = algorithmGenetic.calculateFitness(population, dissimilarityMatrix, numberOfCluster)
    populations.append(population)
    populationsFitness.append(np.sum(populationFitness))

# for index in range(len(populations)):
#     print('Fitness da População: ', populationsFitness[index])

for generation in range(0, 100000):
    mutationRate = 25

    fatherIndex = algorithmGenetic.raffleFathersUsingTournament(populations, populationsFitness)
    motherIndex = algorithmGenetic.raffleFathersUsingTournament(populations, populationsFitness)
    childs = algorithmGenetic.fathersCrossover(populations[fatherIndex], populations[motherIndex])
    finalChilds = []
    firstMutantChild = algorithmGenetic.childMutation(childs[0], mutationRate)
    secondMutantChild = algorithmGenetic.childMutation(childs[1], mutationRate)

    finalChilds.append(firstMutantChild)
    finalChilds.append(secondMutantChild)

    childFitness = algorithmGenetic.calculateFitness(finalChilds[0], dissimilarityMatrix, numberOfCluster)
    positionLessFitness = algorithmGenetic.insertChildInPopulationWithElitism(populationsFitness)
    populationsFitness[positionLessFitness] = np.sum(childFitness)
    populations[positionLessFitness] = finalChilds[0]

    childFitness = algorithmGenetic.calculateFitness(finalChilds[1], dissimilarityMatrix, numberOfCluster)
    positionLessFitness = algorithmGenetic.insertChildInPopulationWithElitism(populationsFitness)
    populationsFitness[positionLessFitness] = np.sum(childFitness)
    populations[positionLessFitness] = finalChilds[1]

    print('Generation: ', generation, 'Best Fitness: ', min(populationsFitness))

finalPopulation = min(populations)
contExibition = 0
print('-----------------------------')
for lineResultIndex in range(0, len(finalPopulation)):
    contExibition = contExibition + 1
    print(finalPopulation[lineResultIndex])
    if(contExibition == 4):
        print('-----------------------------')
        contExibition = 0

# print(np.matrix(min(populations)))
# print(np.matrix(max(populations)))
# print(np.matrix(populationFitness))
