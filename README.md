# Gentic Algorithm for Travelling Salesman Problem


## Travelling Salesman Problem
The Travelling Salesman Problem, or TSP for short, is a problem where given a list of cities and the distances between each cities, what is the shortest path a salesman can take to travel each city once and arrive back to the origin city?

This problem cannot be solved using an exhaustive search as it would take too long to compute especially if the number of cities is not tiny, since the time complexity increases exponentially with the number of cities. Thus this problem is typically solved using approximation algorithms that output an approximation of the answer which might not be the optimal answer but is very close to it.


## Genetic Algorithm
The genetic algorithm is an approximation algorithm that mimics the survival of the fittest in nature. 

The genetic algorithm consists of the following steps:
1. Encoding: A suitable encoding is found to represent a solution
2. Evaluation: The initial population is then selected, the fitness of each solution in the population is computed.
3. Crossover: Two individual solutions are recombined to create new individuals which are copied into the new generation.
4. Mutation: Some individuals are chosen at random and then a mutation point is randomly chosen. The character in the corresponding position is changed.
5. Decoding: A new generation is formed and the steps 2-5 are repeated until a certain criteria is met, in which case the best solution at the time is selected.

