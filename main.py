"""
Due to this being a rush job for fun, don't expect the best results or anything... but it should work :D
"""

# replace this line for your own custom anagram words.
from hyperx import PRODUCTS as CUSTOM_WORDS


def find_anagram(hint: str):
    """
    Searches CUSTOM_WORDS keys to find an anagram of the hint
    :param hint: The original anagram
    :return: a dict of {number_wrong (lower=better): [words]}
    """
    possible_ans = {}
    hint = hint.replace(" ", "")
    possible_prods = (CUSTOM_WORDS.keys())
    hint = hint.upper()
    for k in possible_prods:
        num_wrong = 0
        save = k
        k = k.replace(" ", "")
        for i in hint:
            if i in k:
                k = k.replace(i, "", 1)
            else:
                num_wrong += 1
        num_wrong += len(k)
        if num_wrong not in possible_ans.keys():
            possible_ans[num_wrong] = [save]
        else:
            possible_ans[num_wrong].append(save)
    return possible_ans


def print_solution(solution: dict):
    """
    Prints the solution given by find_anagram in a quicker way to read
    :param solution: The solution given by find_anagram
    """
    for k in sorted(solution.keys()):
        print(k, "incorrect chars")
        for i in solution[k]:
            print(i, CUSTOM_WORDS[i])
        print()


if __name__ == '__main__':
    ans = find_anagram(input("What is the anagram? "))
    print(ans[0][0], CUSTOM_WORDS[ans[0][0]])
    print()
    print_solution(ans)
