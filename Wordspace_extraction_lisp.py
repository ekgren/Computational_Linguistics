'''
File for extracting vectors and names from word spaces in lisp list format
'''


import time
import numpy as np
import re
import codecs


def wordimport(infile):
    stopwords = set()
    with codecs.open(infile, 'r', 'utf-8') as stop_file:
        for line in stop_file:
            line = re.sub(r'\n', '', line)
            line = re.sub(r'\r', '', line)
            stopwords.add(line)
    return stopwords


def fileextraction(filepath, max_points, dimension, min=0, max=10000000,
                   wordlist=None, start=0):

    raw = open(filepath)
    points_added = 0
    jump_lines = 0
    vectorlist = []
    for vector in raw:
        if jump_lines < start:
                jump_lines += 1
        else:
            if points_added == max_points:
                break

            if wordlist != None:
                store = statemachine(vector, dimension, 0, 10000000)
            else:
                store = statemachine(vector, dimension, min, max)
            if store and wordlist == None:
                vectorlist.append(store)
                points_added += 1
            elif store and store[0] in wordlist:
                vectorlist.append(store)
                points_added += 1
    raw.close()

    return vectorlist


def statemachine(string, dimension, min=0, max=10000000):

    instances = ""
    state = 0
    for n in range(-20, 0):
        if state == 0:
            if string[n] == ":":
                state = 1
        elif state == 1:
            if string[n] == ")":
                break
            elif string[n] == "#":
                state = 2
            elif string[n] != " ":
                instances += string[n]
        elif state == 2:
            if string[n] == ";":
                state = 0
            elif string[n] == ":":
                return 0

    instances = int(instances)

    if instances > min and instances < max:
        '''
        States:
        START = 0
        NAME = 1
        WORD_DIMENSION = 2
        WORD_VECTOR = 3
        CONTEXT_DIMENSION = 4
        CONTEXT_VECTOR = 5
        END = 6
        '''
        ## Local variables
        state = 0
        sign = 0
        index = ""
        weight = ""

        ## Return variables
        name = []
        word_dimension = dimension
        context_dimension = dimension
        word_vector = []
        context_vector = []

        for char in string:
            if state == 0:
                if char == '"':
                    state = 1

            elif state == 1:
                if char == '"':
                    state = 2
                else:
                    name.append(char)

            elif state == 2:
                if char == ";":
                    state = 3

            elif state == 3:
                if char == ":":
                    state = 4
                    word_vector.append((int(index), sign * float(weight)))
                    sign = 0
                    index = ""
                    weight = ""
                else:
                    if sign == 0:
                        if char == "+":
                            sign = 1
                        elif char == "-":
                            sign = -1
                        else:
                            index += char
                    else:
                        if char == ";":
                            word_vector.append((int(index), sign *
                                                float(weight)))
                            sign = 0
                            index = ""
                            weight = ""
                        else:
                            weight += char

            elif state == 4:
                if char == ";":
                    state = 5
                elif char == ":":
                    state = 6

            elif state == 5:
                if char == ":":
                    state = 6
                    context_vector.append((int(index), sign * float(weight)))
                    sign = 0
                    index = ""
                    weight = ""
                else:
                    if sign == 0:
                        if char == "+":
                            sign = 1
                        elif char == "-":
                            sign = -1
                        else:
                            index += char
                    else:
                        if char == ";":
                            context_vector.append((int(index), sign *
                                                   float(weight)))
                            sign = 0
                            index = ""
                            weight = ""
                        else:
                            weight += char

        return (''.join(name), word_dimension, word_vector, context_dimension,
                context_vector, instances)
    else:
        return 0

if __name__ == '__main__':
    
    START = 0                           # Starting point
    MAX_POINTS = 10000000               # maximum points to extract
    MIN = 3                             # minimum word frequency
    MAX = 4000                          # maximum word frequency
    DIMENSION = 3000                    # vector dimension
    FILENAME = 'tasa_smaller_and_to'    # name of file
    # WORDLIST = wordimport('../../wordlists/finance_words.txt')
    WORDLIST = ['and','to']

    x = time.time()
    v = fileextraction("../../wordspaces/tasa-smaller.wordspace",
                       MAX_POINTS, DIMENSION, MIN, MAX, WORDLIST, START)

    print("Det tog " + str(time.time() - x) + " sek att ta ut orden")

    x = time.time()
    frequency = np.zeros((len(v)))
    words = np.zeros((len(v)), np.dtype)
    freq = np.zeros((len(v)), np.dtype)
    matrix = np.zeros((len(v), DIMENSION), np.int8)

    for n, item in enumerate(v):
        words[n] = v[n][0]
        freq[n] = v[n][-1]
        for pair in item[4]:
            matrix[n][pair[0]] = pair[1]

    print "Det tog ", time.time() - x, " sek att stoppa in dem i en", np.shape(
        matrix), "matris"

    x = time.time()
    np.save('npy_files/' + FILENAME, matrix)
    np.save('npy_files/' + FILENAME + 'words', words)
    np.save('npy_files/' + FILENAME + 'freq', freq)
    print "Det tog", time.time() - x, "att spara matrisen i filen ", FILENAME

    print("DONE!")
