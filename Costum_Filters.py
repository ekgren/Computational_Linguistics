'''
'''

import numpy as np

from scipy.spatial import distance


def synonym_filter(WordVectors_npArray, WordLabels_npArray):
    '''
    '''
    
    
    pass

def synonym_alternatives_range(WordVectors_npArray, 
                                AlternativesVectorOne_npArray,
                                AlternativesVectorTwo_npArray,
                                AlternativesVectorThree_npArray,
                                AlternativesVectorFour_npArray):
    '''
    '''
    
    
    synonym_alternatives_range = np.zeros(len(WordVectors_npArray))
    
    for word_int in range(len(WordVectors_npArray)):
        
        DistToAltOne = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorOne_npArray[word_int,:])
        print(DistToAltOne)
        DistToAltTwo = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorTwo_npArray[word_int,:])
        print(DistToAltTwo)
        DistToAltThree = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorThree_npArray[word_int,:])
        print(DistToAltThree)
        DistToAltFour = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorFour_npArray[word_int,:])
        print(DistToAltFour)
        
        synonym_alternatives_range[word_int] = (max(DistToAltOne, \
        DistToAltTwo, DistToAltThree, DistToAltFour) - min(DistToAltOne, \
        DistToAltTwo, DistToAltThree, DistToAltFour))
        
    
    return synonym_alternatives_range
    
def synonym_alternatives_average(WordVectors_npArray, 
                                AlternativesVectorOne_npArray,
                                AlternativesVectorTwo_npArray,
                                AlternativesVectorThree_npArray,
                                AlternativesVectorFour_npArray):
    '''
    '''
    
    
    synonym_alternatives_average = np.zeros(len(WordVectors_npArray))
    
    for word_int in range(len(WordVectors_npArray)):
        DistToAltOne = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorOne_npArray[word_int,:])
        print(DistToAltOne)
        DistToAltTwo = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorTwo_npArray[word_int,:])
        print(DistToAltTwo)
        DistToAltThree = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorThree_npArray[word_int,:])
        print(DistToAltThree)
        DistToAltFour = distance.cosine(WordVectors_npArray[word_int,:], \
        AlternativesVectorFour_npArray[word_int,:])
        print(DistToAltFour)
        
        synonym_alternatives_average[word_int] = (DistToAltOne +\
        DistToAltTwo + DistToAltThree + DistToAltFour)/4
        
    return synonym_alternatives_average
    
    

def nth_neighbor_filter():
    ''' Maybe we won't have this.
    '''
    
    
    pass
