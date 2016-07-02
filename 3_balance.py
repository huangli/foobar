def answer(x):

    def get_weight(x):
        if (x <= 4):
            return 1
        else:
            weight = 1
            while x > (pow(3, weight+1) - 1)/2:
                weight += 1
            return weight

    # initialize the list
    to_measure = x
    weight = get_weight(to_measure)
    print "the number has a weight of : " + str(weight)
    result = ['-'] * (weight+1)
    result[weight] = 'R'

    remain = pow(3, weight) - to_measure
    while abs(remain) > 1:
        weight = get_weight(abs(remain))
        if weight > 0:
            result[weight-1] = 'L'
        else:
            result[weight-1] = 'R'
        to_measure = abs(remain)
        remain = pow(3, weight) - to_measure

    if remain == 1:
        result[0] = 'R'
    else:
        result[0] = 'L'

    return ''.join(result)


if __name__ == "__main__":
    # print get_weight(3281)
    print answer(8)
