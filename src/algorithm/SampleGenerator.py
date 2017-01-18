__author__ = 'gbanusi'

import random

out_file = open("file", "w")

i = 0

txt = str(2 ** 17)
for j in range(0, 2 ** 17):
    txt += "\n" + str(random.random()*100)

out_file.write(txt)
