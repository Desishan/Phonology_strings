import pandas as pd


class WordlistPair:
    def __init__(self, source, list1, list2):
        self.source = source
        self.list1 = list1
        self.list2 = list2

    def __str__(self):
        return f'{self.source}'

#this would probably be better if these were built in as a pair.
Pair1 = WordlistPair('Ex2.2Set1: Sanskrit to Pali',
                    ['sasa', 'keːʃa', 'deːʃa', 'doːʂa', 'daːʂa', 'ʃiʂja', 'sasja'],
                    ['sasa', 'kesa', 'desa', 'dosa', 'dasa', 'sissa', 'sassa'])

Pair2 = WordlistPair('Ex2.2Set2: Sanskrit to Pali',
                    ['snaːna', 'sneha', 'snihyati', 'snigdha'],
                    ['sinaːna', 'sineha', 'sinihyati', 'siniddha'])

pair3 = {
    "Sanskrit": ['aːʂadha', 'kaːuʃika'],
    "Pali": ['oːsadha', 'koːsika']
}

dfpair3 = pd.DataFrame(pair3)

print(dfpair3)

exit()