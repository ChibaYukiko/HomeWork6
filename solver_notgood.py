#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    #print dist

    current_city = 0
    #last_city = 0
    sum_kyori1 = 0
    sum_kyori2 = 10000000
    unvisited_cities = set(range(1, N))
    solution = [current_city]
    min_solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    patern = [[1,2,3,4,0],[1,2,4,3,0],[1,3,2,4,0],[1,3,4,2,0],[1,4,2,3,0],[1,4,3,2,0],[2,1,3,4,0],[2,1,4,3,0],[2,3,1,4,0],[2,3,4,1,0],[2,4,1,3,0],[2,4,3,1,0],[3,1,2,4,0],[3,1,4,2,0],[3,2,1,4,0],[3,2,4,1,0],[3,4,1,2,0],[3,4,2,1,0],[4,1,2,3,0],[4,1,3,2,0],[4,2,1,3,0],[4,2,3,1,0],[4,3,1,2,0],[4,3,2,1,0]]

    for i in range(0,24):
        #print "24 starts"
        for j in range(0,5):
            #print "5 start"
            sum_kyori1 += distance_from_current_city(patern[i][j])
            current_city = patern[i][j]
            solution.append(current_city)
            
        #print sum_kyori1    
        if sum_kyori2 > sum_kyori1:
            sum_kyori2 = sum_kyori1
            min_solution = solution

        current_city = 0
        sum_kyori1 = 0
        solution = [current_city]

    print "min :"
    print  sum_kyori2
    return min_solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
