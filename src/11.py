import collections
import re as regexp

words = regexp.sub(r"[!,.?;:#$%^&*()]", "", input().lower()).split()
word_to_number_of = collections.Counter(words)


def is_right_word(word: str) -> bool:
    return word_to_number_of.get(word, 0) > 2 and len(word) > 4 and len(set(word)) > 3


print(*sorted(set(filter(is_right_word, words))), sep="\n")
