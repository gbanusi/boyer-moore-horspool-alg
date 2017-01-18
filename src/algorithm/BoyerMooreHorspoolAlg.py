from src.algorithm.Preprocess import compute_shift_table

__author__ = 'gbanusi'


def boyer_moore_horspool(text, pattern):
    # text length
    text_length = len(text)

    # pattern length
    pattern_length = len(pattern)

    if text_length < pattern_length:
        return -1

    # table of last occurrence of letter in pattern
    last_occurrence = compute_shift_table(pattern)

    # line pattern up at T[0]
    start_point = 0

    # starting point added with pattern length are lower than text length
    while start_point + pattern_length <= text_length:

        # start at the last char in pattern
        j = pattern_length - 1

        # check whether the word is correct
        while pattern[j] == text[start_point + j]:
            # check "next" (= previous) character
            j -= 1

            if j < 0:
                # pattern found!
                return start_point

        # set the pattern on the last occurrence of the first compared letter
        start_point = start_point + last_occurrence[ord(text[start_point + pattern_length - 1])]

    return -1
