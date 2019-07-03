import random
import numpy as np
import ImagesManager as imageManager

class GeneticAlgorithm:

    def initRandomPopulation(self, amountPopulation, amountClusterings):
        population = [[0 for personCluster in range(amountClusterings)] for personInPopulation in range(amountPopulation)]
        for personInPopulation in range(amountPopulation):
            initRandom = 0
            finalRandom = amountClusterings - 1
            positionCluster = random.randint(initRandom, finalRandom)
            population[personInPopulation][positionCluster] = 1
        return population

    # def calculateFitness(self, population):
    #     return False
    #
    # def raffleFathersUsingTournament(self, population, allFitness):
    #     selectedFathers = []
    #     selectedFitnessFathers = []
    #
    #     allFathersSorted = False
    #     positionsRaffled = []
    #     while (allFathersSorted == False):
    #         canSelectFather = True
    #         initRandom = 0
    #         finalRandom = len(population[0])
    #         selectedPosition = random.randint(initRandom, finalRandom)
    #
    #         for index in range(len(positionsRaffled)):
    #             if(positionsRaffled[index] == selectedPosition):
    #                 canSelectFather = False
    #                 break
    #             else:
    #                 canSelectFather = True
    #
    #         if(canSelectFather):
    #             positionsRaffled.append(selectedPosition)
    #             selectedFathers.append(population[selectedPosition])
    #             selectedFitnessFathers.append(allFitness[selectedPosition])
    #
    #         if(len(selectedFathers) == 3):
    #             allFathersSorted = True
    #
    #     betterFather = []
    #     betterFitness = -100000
    #     for indexFather in range(len(selectedFathers)):
    #         # print(selectedFitnessFathers[indexFather], selectedFitnessFathers[indexFather] > betterFitness)
    #         if(selectedFitnessFathers[indexFather] > betterFitness):
    #             betterFitness = selectedFitnessFathers[indexFather]
    #             betterFather = selectedFathers[indexFather]
    #
    #     return betterFather
    #
    # def fathersCrossover(self, father, mother):
    #     childs = []
    #     amountChildGenes = len(father)
    #
    #     clusterAdded = False
    #     childInDevelopment = []
    #     for geneIndex in range(amountChildGenes):
    #         if (clusterAdded):
    #             childInDevelopment.append(0)
    #         else:
    #             if (geneIndex < amountChildGenes // 2):
    #                 childInDevelopment.append(father[geneIndex])
    #                 if (father[geneIndex] == 1):
    #                     clusterAdded = True
    #             else:
    #                 childInDevelopment.append(mother[geneIndex])
    #                 if (mother[geneIndex] == 1):
    #                     clusterAdded = True
    #     childs.append(childInDevelopment)
    #
    #     clusterAdded = False
    #     childInDevelopment = []
    #     for geneIndex in range(amountChildGenes):
    #         if (clusterAdded):
    #             childInDevelopment.append(0)
    #         else:
    #             if (geneIndex < amountChildGenes // 2):
    #                 childInDevelopment.append(father[geneIndex])
    #                 if (father[geneIndex] == 1):
    #                     clusterAdded = True
    #             else:
    #                 childInDevelopment.append(mother[geneIndex])
    #                 if (mother[geneIndex] == 1):
    #                     clusterAdded = True
    #
    #     childs.append(childInDevelopment)
    #
    #     return childs
    #
    # def childMutation(self, child):
    #     initRandom = 0
    #     finalRandom = 10
    #     canMutation = random.randint(initRandom, finalRandom)
    #     childMutant = []
    #     if(canMutation < 1000):
    #         for indexGene in range(len(child)):
    #             childMutant.append(0)
    #         genePosition = random.randint(initRandom, len(childMutant) -1)
    #         childMutant[genePosition] = 1
    #     if(len(childMutant) == 0):
    #         return child
    #     else:
    #         return childMutant
    #
    # def insertChildInPopulationWithElitism(self, population, child):
    #     return False



dissimilarityMatrix = imageManager.getDissimilarityMatrixImagesForClustering(15, 'Images')
algorithmGenetic = GeneticAlgorithm()
population = algorithmGenetic.initRandomPopulation(len(dissimilarityMatrix), 4)

print(np.matrix(population))
