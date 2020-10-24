

class CribFinder:

    def __init__(self, code):
        self._code = code

    def find_crib_in_code(self, crib):
        potential_codes = []
        for starting_position in range(len(self._code) - len(crib)):
            potential_code = ""
            for char_indx, char in enumerate(crib):
                code_letter = self._code[starting_position + char_indx]
                if char == code_letter:
                    break
                potential_code = potential_code + code_letter
            if len(potential_code) == len(crib):
                potential_codes.append(potential_code)
        return potential_codes

