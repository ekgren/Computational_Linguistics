'''
'''
import Costum_Filters

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
        self.WordlistIndexes_npArray = None
        
        self.ExtraWords_npArray = None
        
        self.WordFilterValues_npArray = None
    
    
    def add_wordlist(self, DirectoryPath_str):
        '''Assuming that the list of words is a .txt file 
        with one word per line. '''
        
        
        Local_Wordlist_list = []
        raw_file = open(DirectoryPath_str)
        
        for line_str in raw_file:
            Local_Wordlist_list.append(line_str.split()[0])
        
        raw_file.close()
        
        self.Wordlist_npArray = np.array(Local_Wordlist_list)
        self.index_finder()
    
    
    def index_finder(self):
        '''Method that finds the indexes of the vectors 
        from wordlist. '''
    
        
        Indexes_npArray = np.zeros(len(self.Wordlist_npArray))
        
        for m_int, Key_str in enumerate(self.Wordlist_npArray):
        
            MissingValue_bol = True
            
            for n_int, Word_str in enumerate(self.WordLabels_npArray):
                
                if Word_str == Key_str:
                    Indexes_npArray[m_int] = n_int
                    MissingValue_bol = False
            
            if MissingValue_bol:
                Indexes_npArray[m_int] = None
                
        self.WordlistIndexes_npArray = Indexes_npArray
        
        
    def n_neighbors(self, NEIGHBORS_int=10):
        '''
        '''
        
        for VectorIndex_int in self.WordlistIndexes_npArray:
            DistanceVector_npArray = np.ones(len(self.WordVectors_npArray), 
                                             dtype=np.float32)
            
            for n_int, Vector_npArray in enumerate(self.WordVectors_npArray):
                
                Distance_float = self.cosine_distance(Vector_npArray, 
                                         self.WordVectors_npArray[
                                                    VectorIndex_int])
            
                DistanceVector_npArray[n_int] = Distance_float
            
            Neighbors_list = []
            
            for NEIGHBOR_int in range(NEIGHBORS_int):
                
                MinIndex_int = DistanceVector_npArray.argmin()
                
                if MinIndex_int != VectorIndex_int:
                    Neighbors_list.append(MinIndex_int)
                
                DistanceVector_npArray[MinIndex_int] = np.inf
            
            if self.ExtraWords_npArray == None:
                self.ExtraWords_npArray = np.array(Neighbors_list)
            else:
                self.ExtraWords_npArray = np.append(self.ExtraWords_npArray, 
                                                    np.array(Neighbors_list))
    
    
    def cosine_distance(self, v1_npArray, v2_npArray, dtype=np.int32):
        '''
        '''
        
        
        LocalDist_float = distance.cosine(np.array(v1_npArray, dtype=dtype),
                                          np.array(v2_npArray, dtype=dtype))
        
        return LocalDist_float
    
    
    def save_subset(self, DirectoryPath_str):
        '''
        '''
        
        
        if self.ExtraWords_npArray != None:
               TotalIndexes_npArray = np.append(self.Wordlist_npArray, 
                                                self.ExtraWords_npArray)
        else:
            totalIndexes_npArray = self.Wordlist_npArray
            
        totalIndexes_npArray = np.array(totalIndexes_npArray, dtype = np.int)
            
        SubsetVectors_npArray = self.WordVectors_npArray[totalIndexes_npArray]
        SubsetWords_npArray = self.WordLabels_npArray[TotalIndexes_npArray]
        
        np.save(DirectoryPath_str, SubsetVectors_npArray)
        np.save(DirectoryPath_str, SubsetWords_npArray)