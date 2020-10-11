from string import ascii_uppercase


def alpha_to_number(letter):
    return ascii_uppercase.index(letter)


def number_to_alpha(number):
    return ascii_uppercase[number]

