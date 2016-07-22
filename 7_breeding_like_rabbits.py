cache = {0:1, 1:1, 2:2}

def answer(str_S):
    even_idx , odd_idx = 0, 1
    result = int(str_S)
    temp_even = breeding(even_idx)

    while temp_even < result:
        even_idx += 2
        temp_even = breeding(even_idx)

    temp_odd = breeding(odd_idx)
    while temp_odd < result:
        odd_idx += 2
        temp_odd = breeding(odd_idx)

    if temp_odd == result and temp_even == result:
        return max(even_idx, odd_idx)
    elif temp_odd == result and temp_even != result:
        return odd_idx
    elif temp_odd != result and temp_even == result:
        return even_idx
    else:
        return 'None'



def breeding(n):
    if n in cache:
        return cache[n]
    else:
        if n % 2 == 0:
            m = n / 2
            cache[n] = breeding(m) + breeding(m+1) + m
        else:
            m = (n-1) / 2
            cache[n] = breeding(m-1) + breeding(m) + 1

    return cache[n]


if __name__ == "__main__":
    # print answer(7)
    # print answer(str(10**25))
    for i in range(40):
        # if i % 2 == 0:
        print "i: " + str(i) + ", " + str(breeding(i))
