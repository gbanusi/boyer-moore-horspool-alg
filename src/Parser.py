__author__ = 'gbbanusic'


def parseTestCases(file):

    dict = []
    pattern = []
    text = []

    with open(file) as stream:
        pt = ""
        tt = ""
        for line in stream:
            if line == "\n":
                pattern.append(pt)
                text.append(tt)
                pt = ""
                tt = ""

            elif line.startswith('pattern:'):
                pt = line.split(":")[1].strip()

            elif line.startswith('text:'):
                tt += line.split(":")[1].strip()

            else:
                tt += line.strip()

    stream.close()

    for i in range(0, len(pattern)):
        dict.append([pattern[i], text[i]])

    return dict