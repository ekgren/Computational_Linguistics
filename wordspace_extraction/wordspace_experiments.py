import numpy as np
import Wordspace_Extraction as we

wordspace_path = "../gavagai-bncpluslobo.wordspace"
allWordsText = "data/every_word.txt"

extraction = we.Wordspace_Extraction(wordspace_path)

extraction.extract_vocabulary()
difference, intersection = extraction.check_wordlist(allWordsText)

print(difference)
print()
print(intersection)
