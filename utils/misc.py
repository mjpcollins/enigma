from string import ascii_uppercase


def alpha_to_number(letter):
    return ascii_uppercase.index(letter)


def number_to_alpha(number):
    return ascii_uppercase[number]


def shift_letter(letter, number):
    num_of_letter = alpha_to_number(letter)
    shifted = (num_of_letter + number) % 26
    return number_to_alpha(shifted)
