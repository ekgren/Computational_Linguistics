'''
'''
import Costum_Filters

import numpy as np
from scipy.spatial import distance

class Wordspaceprocessing:
    def __init__(self,
                 WordVectors_npArray=None, 
                 WordLabels_npArray=None,
                 DebugMode_bol = True):
        '''
        '''
        
        self.DebugMode_bol = DebugMode_bol
        
        self.WordVectors_npArray = WordVectors_npArray
        self.WordLabels_npArray = WordLabels_npArray
        
        self.Wordlist_npArray = None
        self.WordlistIndexes_npArray = None
        
        self.ExtraWords_npArray = None
        
        self.TotalIndexes_npArray = None
        
        self.WordFilterValues_npArray = None
        
    def add_all_words(self):
        self.Wordlist_npArray = self.WordLabels_npArray
        self.WordlistIndexes_npArray = np.arange(len(self.WordVectors_npArray))
        self.TotalIndexes_npArray = self.WordlistIndexes_npArray
    
    
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
        
        Indexes_npArray = Indexes_npArray[np.logical_not(
                                        np.isnan(Indexes_npArray))]
        self.WordlistIndexes_npArray = np.sort(np.array(Indexes_npArray,
                                                        dtype = np.int32))
        
        self.TotalIndexes_npArray = self.WordlistIndexes_npArray.copy()
        
        self.Wordlist_npArray = self.WordLabels_npArray[
                                        self.WordlistIndexes_npArray]
        
        
    def n_neighbors(self, NEIGHBORS_int=10):
        '''
        '''
        
        
        if self.DebugMode_bol:
            Length_int = len(self.WordlistIndexes_npArray)
            Counter_int = 1
            print("Finding and adding nth nearest neighbors.")
        
        for VectorIndex_int in self.WordlistIndexes_npArray:
            DistanceVector_npArray = self.distance_vector(VectorIndex_int)
            
            Neighbors_list = []
            
            for NEIGHBOR_int in range(NEIGHBORS_int):
                
                MinIndex_int = DistanceVector_npArray.argmin()
                
                if MinIndex_int != VectorIndex_int:
                    Neighbors_list.append(MinIndex_int)
                
                DistanceVector_npArray[MinIndex_int] = np.inf
            
            if self.ExtraWords_npArray == None:
                self.ExtraWords_npArray = np.array(Neighbors_list)
            else:
                self.ExtraWords_npArray = np.append(
                                        self.ExtraWords_npArray, 
                                        np.array(Neighbors_list))
            if self.DebugMode_bol:
                print('Processing ' + str(Counter_int) + ' of ' + 
                      str(Length_int))
                Counter_int = Counter_int + 1
        
        if self.ExtraWords_npArray != None:
               self.TotalIndexes_npArray = np.append(
                                                self.WordlistIndexes_npArray, 
                                                self.ExtraWords_npArray)
        else:
            self.TotalIndexes_npArray = self.WordlistIndexes_npArray
            
        self.TotalIndexes_npArray = np.array(
                                        np.sort(self.TotalIndexes_npArray), 
                                        dtype=np.int32)
    
    
    def cosine_distance(self, v1_npArray, v2_npArray, dtype=np.int32):
        '''Compute the cosine distance between two vectors
        and recasts the arrays by chosen data type.'''
        
        
        LocalDist_float = distance.cosine(np.array(v1_npArray, dtype=dtype),
                                          np.array(v2_npArray, dtype=dtype))
        
        return LocalDist_float
    
    def generate_filter(self, FilterName_str, FilterArgument_float,
                        DirectoryPath_str, FileName_str):
        '''
        '''
        
        
        if FilterName_str == 'Radius':
            if self.DebugMode_bol == True:
                print('Started processing Radius filter.')
                
            NeighborCount_npArray = np.zeros(len(self.TotalIndexes_npArray))
            
            for n_int, Index_int in enumerate(self.TotalIndexes_npArray):
                NeighborCount_npArray[n_int] = self.neighbors_radius(Index_int,
                                                        FilterArgument_float)
            
            np.save(DirectoryPath_str + FileName_str, NeighborCount_npArray)
            
            if self.DebugMode_bol == True:
                print('Done processing Radius filter.')
        
        if FilterName_str == 'Nth_neighbor':
            if self.DebugMode_bol == True:
                print('Started processing Nth_neighbor filter.')
            
            Total = len(self.TotalIndexes_npArray)#Change later
            
            NthNeighborDistance_npArray = np.zeros(
                                                len(self.TotalIndexes_npArray))
            for n_int, Index_int in enumerate(self.TotalIndexes_npArray):
                DistanceVector_npArray = self.distance_vector(Index_int)
                for m_int in range(FilterArgument_float + 1):
                    DistanceVector_npArray[DistanceVector_npArray.argmin()] = \
                        np.inf
                NthNeighborDistance_npArray[n_int] = \
                        DistanceVector_npArray.min()
                #print(str(n_int) + " of " + str(Total))
                print(NthNeighborDistance_npArray[n_int])
            
            np.save(DirectoryPath_str + FileName_str, 
                    NthNeighborDistance_npArray)
            
            if self.DebugMode_bol == True:
                print('Done processing Nth_neighbor filter.')
                
        if FilterName_str == 'PCA':
            if self.DebugMode_bol == True:
                print('Started processing PCA filter.')
                
            PCA_npArray = self.PCA()
            PCA_npArray = PCA_npArray[:, FilterArgument_float]
            np.save(DirectoryPath_str + FileName_str, PCA_npArray)
            
            if self.DebugMode_bol == True:
                print('Done processing PCA filter.')
            
            
    def neighbors_radius(self, VectorIndex_int, RADIUS_float):
        '''
        '''
        
        
        NeighborCounter_int = 0
        
        for Vector_npArray in self.WordVectors_npArray:
            Dist_int = self.cosine_distance(Vector_npArray, 
                                     self.WordVectors_npArray[VectorIndex_int]) 
            if Dist_int <= RADIUS_float and Dist_int != 0:
                NeighborCounter_int = NeighborCounter_int + 1
        
        return NeighborCounter_int
    
    
    def distance_vector(self, VectorIndex_int):
        '''
        '''
        
        
        DistanceVector_npArray = np.ones(len(self.WordVectors_npArray), 
                                                 dtype=np.float32)
                
        for n_int, Vector_npArray in enumerate(
                                        self.WordVectors_npArray):
            
            Distance_float = self.cosine_distance(Vector_npArray, 
                                     self.WordVectors_npArray[VectorIndex_int])
        
            DistanceVector_npArray[n_int] = Distance_float
        
        return DistanceVector_npArray
    
    
    def PCA(self):
        import mdp
        pca = mdp.nodes.PCANode(svd=True)
        pca.train(np.array(self.WordVectors_npArray[
                                            self.WordlistIndexes_npArray],
                           dtype=np.float32))
        datap = pca.execute(np.array(
                    self.WordVectors_npArray[self.WordlistIndexes_npArray],
                    dtype = np.float32))
        
        return datap

    
    def save_subset(self, DirectoryPath_str):
        '''Save subsets of the data to file.
        '''
        
        
        if self.TotalIndexes_npArray != None:
            SubsetVectors_npArray = self.WordVectors_npArray[
                                                    self.TotalIndexes_npArray]
            SubsetWords_npArray = self.WordLabels_npArray[
                                                    self.TotalIndexes_npArray]
        elif self.Wordlist_npArray != None:
            SubsetVectors_npArray = self.WordVectors_npArray[
                                                self.WordlistIndexes_npArray]
            SubsetWords_npArray = self.WordLabels_npArray[
                                                self.WordlistIndexes_npArray]
        
        np.save(DirectoryPath_str + 'Vectors', SubsetVectors_npArray)
        np.save(DirectoryPath_str + 'Words', SubsetWords_npArray)
