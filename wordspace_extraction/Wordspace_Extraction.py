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
        '''
        pass

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