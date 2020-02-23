# Module that is responsible to generate text randomly based on the successor of a given word

import time
import sys
import re
from random import choices
from collections import Counter
import text_stats


def main():
    with open(sys.argv[1], "r", encoding="utf8") as file:
        doc = text_stats.data_processing(file)
    sentence = generate_random_sentence(doc)
    print(sentence)


def generate_random_sentence(doc):
    cur_word = sys.argv[2]
    msg = cur_word
    max_word_number = int(sys.argv[3])
    word_counter = 1

    words = doc.split()
    c = dict(Counter(words))

    while word_counter < max_word_number:  # must add this (until there are no successors in cur_word)
        rx = r'%s (\w+){1}' % cur_word
        prog = re.compile(rx)
        c2 = Counter(prog.findall(doc))
        most_common_successors = dict(c2.most_common())
        for key, value in most_common_successors.items():
            most_common_successors[key] = value / c[cur_word]
        selected_successor = choices(population=list(most_common_successors.keys()),
                                     weights=list(most_common_successors.values()), k=1)
        cur_word = selected_successor[0]
        msg = msg + " " + cur_word
        word_counter += 1
    return msg


if __name__ == '__main__':
    start_time = time.time()
    main()
    passed_time = time.time() - start_time
    print(passed_time)
