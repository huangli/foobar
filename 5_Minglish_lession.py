def answer(words):
    words_len = len(words)
    sort_order_dict= {}


    def find_edge(s1, s2):
        min_words_len = min(len(s1), len(s2))
        for i in range(min_words_len):
            if s1[i] != s2[i]:
                return s1[i], s2[i]


    # get sort list
    for i in range(words_len-1):
        edge = find_edge(words[i], words[i+1])
        if edge:
            # print start_node, end_node
            start_node, end_node = edge
            if start_node in sort_order_dict:
                sort_order_dict[start_node].append(end_node)
            else:
                sort_order_dict[start_node] = [end_node]


    # find the start node
    end_nodes = set()
    for nodes in sort_order_dict.values():
        for node in nodes:
            end_nodes.add(node)

    start_node = set()
    for node in sort_order_dict:
        if node not in end_nodes:
            start_node.add(node)

    # add first sort pair
    # print sort_order_dict    temp = start_node.pop()
    result = []
    visited_node = []
    # while sort_order_dict
        # print "round ----:"
        # print sort_order_dict        # print result
    def visit(node):
        # print 'node: ' + node
        if node not in visited_node:
            visited_node.append(node)
            if node in sort_order_dict:
                for edge in sort_order_dict[node]:
                    visit(edge)
            result.append(node)

    visit(start_node.pop())
    return ''.join(result[::-1])


if __name__ == "__main__":
    print answer(["y", "z", "xy"])
    print answer(["z", "yx", "yz"])
    print answer(["dd", "e", "f", "fa", "fb", "fbb", "fbd"])
