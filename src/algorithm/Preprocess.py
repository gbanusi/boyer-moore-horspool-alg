__author__ = 'gbanusi'


def compute_shift_table(pattern):
    pattern_length = len(pattern)
    shift_table = []
    for k in range(0, 255):
        shift_table.append(pattern_length)
    for k in range(0, pattern_length - 1):
        shift_table[ord(pattern[k])] = pattern_length - 1 - k
    return shift_table



