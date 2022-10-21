# Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
from typing import List


def group_by_rhyme(words: List[str]) -> List[List[str]]:
    return [t for t in
            [[words[x] for x in range(y, len(words)) if words[x][-2:] == words[y][-2:] and
              words[x][-2:] not in [words[w][-2:] for w in range(y)]] for y in range(len(words))]
            if len(t) > 0]


if __name__ == '__main__':
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
