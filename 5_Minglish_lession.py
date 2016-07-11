def answer(words):
    words_len = len(words)
    sort_list = []

    # get sort list
    for i in range(words_len-1):
        min_words_len = min(len(words[i]), len(words[i+1]))
        for j in range(min_words_len):
            if words[i][j] != words[i+1][j]:
                sort_list.append([words[i][j],words[i+1][j]])

    # print sort_list
    temp = sort_list.pop()
    result = []
    result.append(temp[0])
    result.append(temp[1])
    remove_list = []
    while sort_list:
        # print "round ----:"
        # print sort_list
        # print result
        for temp in sort_list:
            # raw_input("Press Enter to continue...")
            # print temp
            if temp[0] == result[-1]:
                remove_list.append(temp)
                result.append(temp[1])
            elif temp[1] == result[0]:
                remove_list.append(temp)
                result.insert(0, temp[0])
            elif temp[0] in result and temp[1] in result:
                remove_list.append(temp)
            else:
                pass
        # clear the to be removed list index
        # print "to be removed list"
        # print remove_list
        for temp in remove_list:
            sort_list.remove(temp)
        remove_list = []

    return ''.join(result)



if __name__ == "__main__":
    # print answer(["y", "z", "xy"])
    # print answer(["z", "yx", "yz"])
    print answer(["a", "ba", "bc","c"])
