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
    last_city = 0
    sum_kyori = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        sum_kyori += dist[current_city][next_city]
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    sum_kyori += dist[current_city][last_city]
    print sum_kyori

    found = False

    #solution = list(range(N))

    while True:
        found = False
        for a in range(0,N):
            #print "start a"
            for b in range(a+2, N):
                if a == 0:
                    a2 = N-1
                else :
                    a2 = a-1
                    
                #print "start b"
                kyori1 = dist[solution[a2]][solution[a]]
                kyori2 = dist[solution[b-1]][solution[b]]

                kyori3 = dist[solution[a2]][solution[b-1]]
                kyori4 = dist[solution[a]][solution[b]]
                
                if (kyori1+kyori2) > (kyori3+kyori4):
                    print "found!"
                    solution[a:b] = solution[b-1:a-1:-1]
                    print solution
                    found = True
                    break

            if found:
                print "break"
                break
        if not found:
            break;

    sum_kyori = 0
    for i in range(N-1):
        sum_kyori += dist[solution[i]][solution[i+1]]
    sum_kyori += dist[solution[N-1]][solution[0]]
    print "ko-shin!"
    print sum_kyori
    
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
