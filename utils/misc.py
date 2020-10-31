from string import ascii_uppercase

twenty_six_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                     43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def alpha_to_number(letter):
    return ascii_uppercase.index(letter)


def number_to_alpha(number):
    return ascii_uppercase[number]


def letter_to_prime(letter):
    return twenty_six_primes[alpha_to_number(letter)]
