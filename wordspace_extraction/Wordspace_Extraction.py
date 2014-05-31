'''A class for extracting wordspaces from Gavagai.  '''


class Wordspace_Extraction:
    def __init__(self):
        '''
        '''
        
        self.Wordspace = None
        self.vocabulary_set = set()

    def extract_vocabulary(self, path):
        ''' Extracts vocabulary from word space file.
        '''
        with open('C:/Alpha/wordspaces/gavagai-aclice_adventures.wordspace') as f:
            for line in f:
                s = line.split(" ")
                self.vocabulary_set.add(s[0])
    
    def check_wordlist(self):
        '''Checks if the words in a wordlist is in the wordspace file.  
        '''


    def extract_wordlist(self):
        '''Extracts words from a given wordlist to a wordspace_file.
        '''
        
    def combine(self):
        '''Combines several extracted words into a single file.
        '''
        
    def extract_words(self):
        '''A generic function for extracting words.
        '''
        
    def extract_full(self):
        '''Extracts the full wordspace file loaded into the 
        Wordspace_Extraction.  '''
        
    def save_wordspace(self):
        '''Saves all extracted words in a numpy array.
        '''
