def answer(words):
    words_len = len(words)
    sort_list = []

    # get sort list
    for i in range(words_len-1):
        min_words_len = min(len(words[i]), len(words[i+1]))
        for j in range(min_words_len):
            if words[i][j] != words[i+1][j]:
                sort_list.append([words[i][j],words[i+1][j]])

    result = []
    for i in range(words_len-1):
        # if order exist
        temp = sort_list[i]
        # print "Round: " + str(i)
        # print "result: " + str(result)
        # print "temp " + ''.join(temp)
        if temp[0] in result and temp[1] not in result:
            idx = result.index(temp[0])
            result = result[:idx] + [temp[1]] + result[idx:]
        elif temp[1] in result and temp[0] not in result:
            idx = result.index(temp[1]) - 1
            result = result[:idx] + [temp[0]] + result[idx:]
        # not exist, just append
        elif temp[1] not in result and temp[0] not in result:
            result.append(temp[0])
            result.append(temp[1])
            # insert in the middle
            # insert at the end

    return result



if __name__ == "__main__":
    print answer(["y", "z", "xy"])
    print answer(["z", "yx", "yz"])
