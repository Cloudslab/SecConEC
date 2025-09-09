from typing import List

import numpy as np
import random

choicesA = np.arange(0.7, 0.9, 0.01)
choicesB = np.arange(0.1, 0.3, 0.01)


def generate_matrix(variableNum):
    matrix = np.zeros((variableNum, 2))
    for i in range(variableNum):
        matrix[i, 0] = random.choice(choicesA)
        matrix[i, 1] = random.choice(choicesB)
    return matrix


def randomPopulation(
        lowerBounds: List[int],
        upperBounds: List[int],
        variableNum: int,
        populationSize: int):
    matrix = np.zeros(
        shape=(variableNum, populationSize),
        dtype=int)

    for i in range(variableNum):
        column = np.random.randint(
            low=lowerBounds[i],
            high=upperBounds[i] + 1,
            size=populationSize)
        matrix[i] = column
    indexSequencesRandom = np.transpose(matrix)
    factor_matrix = generate_matrix(populationSize)
    indexSequencesRandom = np.append(indexSequencesRandom, factor_matrix, axis=1)
    # print(indexSequencesRandom)
    return indexSequencesRandom


if __name__ == '__main__':
    lowerBounds = [0, 0, 0]
    upperBounds = [10, 10, 10]
    variableNum = 3
    populationSize = 5
    pop = randomPopulation(lowerBounds, upperBounds, variableNum, populationSize)
    print(pop)
    from pymoo.model.population import Population
    population = Population.new("X", pop)
    print(population)
