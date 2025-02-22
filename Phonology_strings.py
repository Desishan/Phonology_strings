import re
import phono_data

#To do: add case with multiple 'to' results

def print_formula(old_phone_list: list, new_phone: str, cond: str = None, description: str = None):
    """Produce the formula for a sound change in phonological rule notation."""
    patterns = ', '.join(old_phone_list)
    formula = f'{patterns} > {new_phone}'
    if cond is not None:
        formula += f' / {cond}'
    if description is not None:
        formula += f'\n{description}'
    print(formula)
    return formula


def ipa_to_regex(old_phone: str, cond: str = None):
    """Convert phonological rule notation to regex-friendly characters."""
    if cond is None:
        return old_phone  #any instances of this phoneme apply to the change
    else:
        cond_regex = cond
        if old_phone != '∅':  #if old_phone == '∅', we parse cond using the insertion func instead
            cond_regex = cond_regex.replace('_', old_phone)
    cond_regex = re.sub('^#', '^', cond_regex)
    cond_regex = re.sub('#$', '$', cond_regex)
    return cond_regex  #instances of the phoneme that follow the condition apply to the change


def insertion(new_phone: str, cond: str, word: str):
    """Handle cases of insertion: the condition is split at the appropriate point, matches are found for the
    left and right sides of the condition separately, they are checked for adjacency, and i is inserted between them"""
    split_cond = cond.split('_')
    left_cond = split_cond[0]
    right_cond = split_cond[1]
    matches_leftside = re.finditer(f'{left_cond}(?={right_cond})', word)
    slicepoints = [match.end() for match in matches_leftside]
    if not slicepoints:
        return None
    new_word = ''
    prevpoint = 0
    for point in slicepoints:
        new_word += word[prevpoint:point] + new_phone
        prevpoint = point
    new_word += word[prevpoint:]
    return new_word

def assimilation(old_phone: str, new_phone: str, cond: str)
    # e.g. combining j -> k / k_ with j -> s / s_
    # j -> C1 / {k, s}_


def mutation(old_phone_list: list, new_phone: str, wordlist: list, cond: str = None, description: str = None):
    """Accept a list of starting phonemes, change them to one replacement phoneme if found in the given condition,
    print change formula & resulting wordlist.
    """
    prev_wordlist = [word for word in wordlist]
    old_phone_list.sort(reverse=True, key=len)  # Ensures that longer old_phones, which might contain shorter ones, are dealt with first
    for old_phone in old_phone_list:
        newphone_regex = new_phone.replace('∅', '')  # ∅ is the only phonology 'metacharacter' used outside the condition
        cond_regex = ipa_to_regex(old_phone, cond)
        for i, word in enumerate(wordlist):
            if old_phone == '∅':
                insertion_product = insertion(new_phone, cond_regex, word)
                if insertion_product is not None:
                    wordlist[i] = insertion_product
            else:
                matches = re.finditer(cond_regex, word)
                for match_obj in matches:  # this loop goes through non-overlapping matches within 1 word
                    sub_pattern = match_obj.group().replace(old_phone, newphone_regex)
                    wordlist[i] = wordlist[i].replace(match_obj.group(), sub_pattern)
    if wordlist == prev_wordlist:
        return
    print_formula(old_phone_list, new_phone, cond, description)
    print(wordlist)


def sanskrit_to_pali(wordlist):
    """Go through sound changes one by one, printing the results each time."""
    mutation(['∅'], 'i', wordlist, 's_n', description='epenthetic /i/ breaks up consonant clusters')
    mutation(['ʃ', 'ʂ'], 's', wordlist, description='place-merger of sibilants')
    mutation(['j'], 's', wordlist, 's_', 'regressive place assimilation')
    # Used regex metacharacters in this one. this is a placeholder for phoneme sets, i.e. '#CV_'
    mutation(['ː'], '∅', wordlist, '#.{2}_', description='vowel length loss')
    mutation(['g'], 'd', wordlist, '_d', 'progressive place assimilation of stops')
    mutation(['au', 'auː'], 'oː', wordlist, description='monophthongisaton')
    # Forward step: fold the following change into the previous one, as they are the same
    # i.e. multi_mutation([['au', 'auː']['ai', 'aiː'], ['oː', 'eː'], wordlist, description='monophthongisation')
    mutation(['ai', 'aiː'], 'eː', wordlist, description='monophthongisation')
    # I need to define consonants for the following mutation to have a valid condition!
    # mutation(['ː'], '∅', wordlist)
    return wordlist


# Data given in the puzzle:
starting_wordlist = phono_data.pair3_list1
target_wordlist = phono_data.pair3_list2
print(f'starting wordlist:{starting_wordlist}')

# Data being manipulated
working_list = starting_wordlist
working_list = sanskrit_to_pali(working_list)

if working_list == target_wordlist:
    print('It\'s a match!')
else:
    print(f'It\'s not a match! Current wordlist is {working_list}.')
print(f'target:{target_wordlist}')

exit()