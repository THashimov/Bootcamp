# K is not defined. This should be key
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Unterminated string literal
# Oh is escaping the string
# Changed to double quotes
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}

# Too many arguments 
# Changed the keys to a list
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

