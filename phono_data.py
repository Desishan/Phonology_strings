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
    "Sanskrit": ['auːʂadha', 'kauːʃika', 'gaura', 'mauna', 'augʰa', 'taiːla', 'vaiːra', 'ʃaiːla', 'aikja'],
    "Pali": ['oːsadha', 'koːsika', 'goːra', 'moːna', 'oːgʰa', 'teːla', 'veːra', 'seːla', 'ekka']
}

Ex2_2_dict = {
    "Sanskrit": ['sasa', 'keːʃa', 'deːʃa', 'doːʂa', 'daːʂa', 'ʃiʂja', 'sasja', 'snaːna', 'sneha', 'snihyati', 'snigdha',
                 'auːʂadha', 'kauːʃika', 'gaura', 'mauna', 'augʰa', 'taiːla', 'vaiːra', 'ʃaiːla', 'aikja'],
    "Pali": ['sasa', 'kesa', 'desa', 'dosa', 'dasa', 'sissa', 'sassa', 'sinaːna', 'sineha', 'sinihyati', 'siniddha',
                'oːsadha', 'koːsika', 'goːra', 'moːna', 'oːgʰa', 'teːla', 'veːra', 'seːla', 'ekka'],
    "Set": ['I','I','I','I','I','I','I', 'II', 'II', 'II', 'II',
            'III', 'III', 'III', 'III', 'III', 'III', 'III', 'III', 'III']
}

dfpair3 = pd.DataFrame(pair3)
pair3_list1 = dfpair3['Sanskrit'].tolist()
pair3_list2 = dfpair3['Pali'].tolist()
Ex2_2 = pd.DataFrame(Ex2_2_dict)
