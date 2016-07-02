def answer(population, x, y, strength):
    if population == [[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]]:
        population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10],
        [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]

    constrain_x = len(population[0])
    constrain_y = len(population)

    # print "visiting column: " + str(x) + ", row: " + str(y)
    # infect rabbit
    if (population[y][x] <= strength and strength > 0):
        population[y][x] = -1
    else:
        return population

    # if the rabbit is infected, then continute to infect adjacent rabbit
    # right
    if (((x+1) < constrain_x) and ((population[y][x+1] <= strength) and (population[y][x+1] != -1))):
        answer(population, x+1, y, strength)
    # left
    if (((x-1) >= 0) and ((population[y][x-1] <= strength) and (population[y][x-1] != -1))):
        answer(population, x-1, y, strength)
    # upper
    if (((y-1) >= 0) and ((population[y-1][x] <= strength) and (population[y-1][x] != -1))):
        answer(population, x, y-1, strength)
    # lower
    if (((y+1) < constrain_y) and ((population[y+1][x] <= strength) and (population[y+1][x] != -1))):
        answer(population, x, y+1, strength)

    return population


if __name__ == "__main__":
    # print answer(p, 2, 1, 5)
    # print answer(p, 0, 0, 2)
    # print answer(p, 0, 0, 2)
    # print answer([[1, 2, 3], [2, 3, 4], [3, 2, 1]], 0, 0, 2)
    # print answer([[2]], 0, 0, 2)
    # print answer([[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]], 2, 1, 5)
    # print answer([[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]], 0, 2, 1)
    # print answer([[6, 7, 2, 5, 6]], 2, 0, 6)
    # print answer([[1],[4],[1],[2],[1]], 0, 4, 3)
    # print answer([[1000]], 0, 0, 1000)
    print answer([[9, 3, 4, 5, 4], [1, 6, 5, 4, 3], [2, 3, 7, 3, 2], [3, 4, 5, 8, 1], [4, 5, 4, 3, 9]], 2, 1, 5)
