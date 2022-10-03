""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = ',.!?-~'
_letters = 'AEINOQUabdefghijkmnoprstuvwyz'
_letters_ipa = 'ʃʧ↓↑ '


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")


# """ from https://github.com/keithito/tacotron """

# '''
# Defines the set of symbols used in text input to the model.
# '''
# _pad        = '_'
# _punctuation = ',.!?-~'
# _punctuation_zh = '；：，。！？-“”《》、 '
# _letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# _letters_ipa = '-+ʃʧ↓↑ '
# _numbers = '123450'

# # Export all symbols:
# symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa) + list(_numbers) + list(_punctuation_zh)

# # Special symbol ids
# SPACE_ID = symbols.index(" ")


