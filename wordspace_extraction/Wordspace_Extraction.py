import numpy as np

'''A class for extracting wordspaces from Gavagai.  '''


class Wordspace_Extraction:
    def __init__(self, Wordspace_path):
        '''Loads a wordspace from gavagai when initiated. File type should be
         .wordspace.  '''

        self.Wordspace_path = Wordspace_path
        self.Wordspace = None
        self.Vocabulary = set()

    def extract_vocabulary(self):
        ''' Extracts vocabulary from wordspace.
        '''
        with open(self.Wordspace_path) as f:
            for line in f:
                s = line.split(" ")
                self.Vocabulary.add(s[0][2:-1])

    def extract_vectors_from_line(self, line_from_file):
        '''
        Takes a line from wordspace file and returns
        the word, the base and context vectors and the words frequency.
        '''
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
                    base_vector[int(index[:find_minus])] = - int(index[find_minus+1:])


        # Get context vector
        context_vector = np.zeros(dimension, dtype=np.int32)
        context_vector_string = line_from_file[2][:-1].split(";")[1:]

        for index in context_vector_string:
            find_plus = index.find('+')
            if find_plus != -1:
                context_vector[int(index[:find_plus])] = int(index[find_plus+1:])
            else:
                find_minus = index.find('-')
                if index.find('-') != -1:
                    context_vector[int(index[:find_minus])] = - int(index[find_minus+1:])

        # Get frequency
        freq = int(line_from_file[3].rstrip()[:-1])

        return dimension, word, base_vector, context_vector, freq

    def check_wordlist(self):
        '''Checks if the words in a wordlist is in the wordspace file. Returns 
        a list with the words present in the wordspace and a list with the 
        words that are not in the list.  '''
        with open('C:/Alpha/wordlists/anarchism.txt') as f:

            wordlist = set()

            for line in f:
                wordlist.add(line.rstrip())

        wordlist_difference = wordlist.difference(self.extract_vocabulary())
        wordlist_intersection = wordlist.intersection(self
                                                     .extract_vocabulary())

        return wordlist_difference, wordlist_intersection
        
    def extract_wordlist(self):
        '''Extracts words from a given wordlist to a wordspace_file.
        '''
        pass
        
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