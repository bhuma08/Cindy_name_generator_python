# Game

month_dict = {
    'january' : 'garnet',
    'february' : 'amthyst',
    'march' : 'aquamaine',
    'april' : 'diamond',
    'may' : 'emerald',
    'june' : 'pearl',
    'july' : 'ruby',
    'august' : 'periot',
    'september': 'sapphire',
    'october' : 'opal',
    'november' :'topaz',
    'december' : 'turquoise'
}


first_letter_dict = {
    'a': 'willy',
    'b': 'happy feet',
    'c': 'peggy',
    'd': 'peggy',
    'e': 'peggy',
    'f': 'peggy',
    'g': 'peggy',
    'h': 'peggy',
    'i': 'Wheezy',
    'j': 'Wheezy',
    'k': 'Wheezy',
    'l': 'Wheezy',
    'm': 'Wheezy',
    'n': 'Wheezy',
    'o': 'Wheezy',
    'p': 'willy',
    'q': 'happy feet',
    'r': 'happy feet',
    's': 'happy feet',
    't': 'happy feet',
    'u': 'willy',
    'v': 'willy',
    'w': 'willy',
    'x': 'willy',
    'y': 'willy',
    'z': 'willy'
}


print('Welcome to your dragon/penguin name generator ')
name = input(f'Enter your first name\n')
month = input(f'Enter your month of birth\n')
dragon_or_penguin = input(f'Would you like to know your dragon name or penguin name?\n')
month_lower = month.lower()
name_reverse = name [::-1]
name_lower = name.lower()
first_letter_name = name_lower[0]
#print(name_reverse)

#  Dragon name 
def dragon_name (name_reverse, month_lower):
    # compare user input (month_lower) with month dictionary
    month_dict_compare = month_dict[month_lower]
    print(f'{name_reverse} {month_dict_compare}')
#  penguin name 
def penguin_name (first_letter_name, month_lower):
    first_letter_dict_compare = first_letter_dict[first_letter_name]
    print(first_letter_dict_compare)

def compare (name, month):
    if dragon_or_penguin == 'dragon':
        name = name_reverse
        month = month_lower
        return dragon_name(name, month)
    elif dragon_or_penguin == 'penguin':
        name = first_letter_name
        month = month_lower
        return penguin_name(name, month)
    else:
        print('Error')


a = compare (name_reverse, month_lower)
print(a)


