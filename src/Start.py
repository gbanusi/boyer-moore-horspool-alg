import time

from src.Parser import parseTestCases
from src.algorithm.BoyerMooreHorspoolAlg import boyer_moore_horspool

__author__ = 'gbbanusic'

testCases = parseTestCases("/home/gbbanusic/Fakultet/OAA/Projekt/OAAGenSamples.txt")

out = []

for key in testCases:
    start_time = time.time()
    result = boyer_moore_horspool(key[1], key[0])
    out.append([time.time() - start_time, result])

out_file = open("/home/gbbanusic/Fakultet/OAA/Projekt/OAAOutput.txt", "w")

out_file.write("KEYWORD" + "  FOUND AT  " + "  TIME  " + "  TEST LENGTH  " + "\n\n")
i = 0


for key in testCases:
    out_file.write(key[0] + "   " + str(out[i][1]) + "   " + str(out[i][0]) + "  " + str(len(key[1])) + "\n")
    i += 1

out_file.close()
