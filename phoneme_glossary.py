#This may be better as a pandas dataframe...we'll see.

class Phoneme:
    def __init__(self, ipa, vowel):
        self.ipa = ipa
        self.vowel = vowel

    def __str__(self):
        return f'{self.ipa}'

open_central_unrounded = Phoneme('a', 1)
alveolar_fricative_unvoiced = Phoneme('s', 0)

help(list)