# import time
def answer(food, grid):

# food > maxium then return -1
# traverse the tree list
# food_for_zombie: food need for zombie to leavel the room
# result: all the food needed saved in the list
# grid: the grid of the room
# x,y: the row and column index
# return: a list of each road zombie food needed
    cache = dict()
    def remind(food_left, x, y):
        food_left -= grid[x][y]
        if x < 0 or y < 0 or food_left < 0:
            cache[str(x)+','+str(y)+','+str(food_left)] = food+1
            return food+1
        elif x == 0 and y == 0:
            cache[str(x)+','+str(y)+','+str(food_left)] = food_left
            return food_left
        else:
            if str(x)+','+str(y)+','+str(food_left) in cache:
                return cache[str(x)+','+str(y)+','+str(food_left)]
            else:
                cache[str(x)+','+str(y)+','+str(food_left)] = min(remind(food_left, x-1, y), remind(food_left, x, y-1))
                return cache[str(x)+','+str(y)+','+str(food_left)]

    # # minual food ne
    result = remind(food, len(grid)-1, len(grid[0])-1)
    if result <= food:
        return result
    else:
        return -1


if __name__ =="__main__":
    # start_time = time.time()
    # for i in range(1000):
    print answer(7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    print answer(12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]])
    # l1 = [[1,2,3], [4,5,6], [7,8,9]]
    # print answer(35, l1)
    # print answer(12, [[0]])
    # print("--- %s seconds ---" % (time.time() - start_time))
    # print answer(10, l1)
