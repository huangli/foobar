from __future__ import division

def answer(minions):
    num_minions = len(minions)

    sorted_minions = [a/(b/c) for a,b,c in minions]
    return sorted(range(num_minions), key=sorted_minions.__getitem__)


if __name__ == "__main__":
    print answer([[5, 1, 5], [10, 1, 2]])
