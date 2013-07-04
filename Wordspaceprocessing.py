'''
'''

import numpy as np
from scipy.spatial import distance

class Wordspaceprocessing:
    def __init__(self,
                 WordVectors_npArray=None, 
                 WordLabels_npArray=None):
        '''
        '''
        
        self.WordVectors_npArray = WordVectors_npArray
        self.WordLabels_npArray = WordLabels_npArray
        
        self.Wordlist_npArray = None
        self.Wordlist_indexes_npArray = None
    
    
    def add_wordlist(self, DirectoryPath_str):
        '''
        '''
        
        
        Local_Wordlist_list = []
        raw = open(DirectoryPath_str)
        
        for line_str in raw:
            Local_Wordlist_list.append(line_str.split()[0])
        
        raw.close()
        
        self.Wordlist_npArray = np.array(Local_Wordlist_list)
        self.index_finder()
    
    
    def index_finder(self):
        '''Method that finds the indexes of the vectors from wordlist
        '''
    
        
        Indexes_npArray = np.zeros(len(self.Wordlist_npArray))
        
        for m_int, Key_str in enumerate(self.Wordlist_npArray):
        
            MissingValue_bol = True
            
            for n_int, Word_str in enumerate(self.WordLabels_npArray):
                
                if Word_str == Key_str:
                    Indexes_npArray[m_int] = n_int
                    MissingValue_bol = False
            
            if MissingValue_bol:
                Indexes_npArray[m_int] = None
                
        self.Wordlist_indexes_npArray = Indexes_npArray
        
        
    def neighbors_count(self, v_index, no_neigh=10):
        '''
        '''
        
        
        dist_vect = np.ones(len(self.WordVectors_npArray), dtype=np.float32)
        
        for n, row in enumerate(self.WordVectors_npArray):
            
            d = self.cosine_distance(row, self.WordVectors_npArray[v_index])
        
            dist_vect[n] = d
        
        neighbors_list = []
        
        for no in range(no_neigh):
            neighbors_list.append((dist_vect.argmin(),dist_vect.min()))
            dist_vect[dist_vect.argmin()] = np.inf
            
        return neighbors_list
    
    
    def cosine_distance(self, v1_npArray, v2_npArray, dtype=np.int32):
        '''
        '''
        
        
        LocalDist_float = distance.cosine(np.array(v1_npArray, dtype=dtype),
                                          np.array(v2_npArray, dtype=dtype))
        
        return LocalDist_float