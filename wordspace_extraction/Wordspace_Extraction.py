import random
import numpy as np

'''A class for extracting wordspaces from Gavagai.  '''


class Wordspace_Extraction:
    def __init__(self, Wordspace_path):
        '''Loads a wordspace from gavagai when initiated. File type should be
         .wordspace.  '''

        self.Wordspace_path = Wordspace_path
        self.Wordspace = None
        
        self.Dimension = 0
        self.Vocabulary = {}
        
        with open(self.Wordspace_path) as f:
            line_from_file = f.next().split(" ")
            self.Dimension = int(line_from_file[1].split(";")[0][2:])
        
        
    def extract_vocabulary(self):
        ''' Extracts vocabulary from wordspace.
        '''
        with open(self.Wordspace_path) as f:
            for line in f:

                line_from_file = line.split(" ")
                self.Vocabulary[line_from_file[0][2:-1]] = int(
                    line_from_file[3].rstrip()[:-1])

    def extract_vectors_from_line(self, line_from_file):
        '''
        Takes a line from wordspace file and returns
        the word, the base and context vectors and the words frequency.
        '''
        line_from_file = line_from_file.split(" ")
        
        # Get dimension of vectors
        dimension = int(line_from_file[1].split(";")[0][2:])
        
        # Get word of vector
        word = line_from_file[0][2:-1]

        # Get base vector
        base_vector = np.zeros(dimension, dtype=np.int8)
        base_vector_string = line_from_file[1][:-1].split(";")[1:]

        for index in base_vector_string:
            find_plus = index.find('+')
            if find_plus != -1:
                base_vector[int(index[:find_plus])] = int(index[find_plus+1:])
            else:
                find_minus = index.find('-')
                if index.find('-') != -1:
                    base_vector[int(index[:find_minus])] = \
                    - int(index[find_minus+1:])


        # Get context vector
        context_vector = np.zeros(dimension, dtype=np.int32)
        context_vector_string = line_from_file[2][:-1].split(";")[1:]

        for index in context_vector_string:
            find_plus = index.find('+')
            if find_plus != -1:
                context_vector[int(index[:find_plus])] = \
                int(index[find_plus+1:])
            else:
                find_minus = index.find('-')
                if index.find('-') != -1:
                    context_vector[int(index[:find_minus])] = \
                    - int(index[find_minus+1:])

        # Get frequency
        
        freq = int(line_from_file[3].rstrip()[:-1])

        return word, base_vector, context_vector, freq

    def check_wordlist(self, words_path):
        '''Checks if the words in a wordlist is in the wordspace file. Returns 
        a list with the words present in the wordspace and a list with the 
        words that are not in the list.  '''
        with open(words_path) as f:

            wordlist = set()

            for line in f:
                wordlist.add(line.rstrip())

        wordlist_difference = wordlist.difference(set(self.Vocabulary.keys()))
        wordlist_intersection = wordlist.intersection(set(self.Vocabulary
                                                      .keys()))

        return wordlist_difference, wordlist_intersection

    def pull_wordlist(self, size, save_path):
        subset = random.sample(self.Vocabulary, size)
        with open(save_path, "w") as text_file:
            for word in subset:
                text_file.write(word + '\n')
        
    def extract_wordlist(self, words_path):
        '''Extracts words from a given wordlist to a wordspace_file.
        '''
        wordlist = set()
        with open(words_path) as wp:
        
            nWords = 0
            
            for wordLine in wp:
                wordlist.add(wordLine)
                nWords = nWords + 1
            labelVector_npArray = np.zeros(nWords, dtype=np.dtype)
            contextVector_npArray = np.zeros((nWords,1000), dtype=np.int32)
            wordNumber = 0
        wp = wordlist
            
        with open(self.Wordspace_path) as ws:
            
            for line in ws:
                line_from_file = line.split(" ")
                word = line_from_file[0][2:-1]
                for wordLine in wp:
                    
                    if word == wordLine.rstrip():
                        print(word)
                        word, base_vector, context_vector, freq = \
                            self.extract_vectors_from_line(line)
                        labelVector_npArray[wordNumber] = word
                        contextVector_npArray[wordNumber] = context_vector
                        wordNumber = wordNumber + 1
                            
                        
        return labelVector_npArray, contextVector_npArray
        
    def combine(self):
        '''Combines several extracted words into a single file.
        '''
        pass
        
    def extract_words(self):
        '''A generic function for extracting words.
        '''
        pass
        
    def extract_full(self):
        '''Extracts the full wordspace file loaded into the 
        Wordspace_Extraction.  '''
        pass
        
    def save_wordspace(self):
        '''Saves all extracted words in a numpy array.
        '''
        pass

if __name__ == "__main__":
    pass
