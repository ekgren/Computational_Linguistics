'''
Created on 15 jul 2013

@author: Ariel
'''

import Wordspaceprocessing as W
import numpy as np

name = 'alice'
data = np.load('C:/Alpha/eclipse/Computational_linguistics/npy_files/' + name + '_vectors.npy')  
words = np.load('C:/Alpha/eclipse/Computational_linguistics/npy_files/' + name + '_words.npy')

WS = W.Wordspaceprocessing(data, words, DebugMode_bol = True)

# Wordlist should be a .txt file with one word per line
WS.add_wordlist('C:/Alpha/wordlists/swadesh.txt')

'''
# Here we have different filter functions that can be generated
WS.generate_filter('Radius', 0.8, 'npy_files/', 'tasa_smaller_syn_radius_filt')
WS.generate_filter('Nth_neighbor', 4, 'npy_files/', 'freud_neighb_filt')
WS.generate_filter('PCA', 0, 'npy_files/', 'freud_swadesh_PCA_filt')
'''

WS.save_subset('npy_files/' + name + '_swadesh')