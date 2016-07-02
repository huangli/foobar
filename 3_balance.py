from math import log,ceil

def answer(x):

    def get_level(x):
        num = abs(x)
        if (num == 1):
            return 0
        elif num <= 4:
            return 1
        else:
            level = 1
            while num > (pow(3, level+1) - 1)/2:
                level += 1
            return level

    # initialize the list
    left = [x]
    right = []
    difference = -x
    while difference != 0:
        level = get_level(difference)
        # right is bigger
        if difference > 0:
        # left is bigger
            left.append(pow(3, level))
        else:
            right.append(pow(3, level))
        difference = sum(right) - sum(left)

    # turn into weight
    # print left
    # print right

    result = ['-'] * (get_level(x) + 1)
    # remove itself
    left.remove(x)
    for c in left:
        result[int(ceil(log(c, 3)))] = 'L'
    for c in right:
        result[int(ceil(log(c, 3)))] = 'R'
    return result


if __name__ == "__main__":
    # print get_level(3281)
    # print (answer(122))
    left = 0
    right = 0
    for i in range(1000):
        result = ''.join(answer(i+1))
        # print "number : " + str(i) + ", result: " + ''.join(answer(i))
        # print result
        len_result = len(result)
        for j in range(len_result):
            if result[j] == 'L':
                left += pow(3, j)
            elif result[j] == 'R':
                right += pow(3, j)
            else:
                pass
        if left + i + 1 == right:
            print "correct! number : " + str(i+1) + ", result: " + result
        else:
            print "wrong! number : " + str(i+1) + ", result: " + result
        left = 0
        right = 0

    # print "number : " + str(865) + ", result: " + ''.join(answer(865))

