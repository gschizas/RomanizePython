# -*- coding: utf-8 -*-

__author__ = 'George Schizas'
__version__ = (1, 0)

"""
This is the "romanize" module.

The romanize module supplies one function, romanize().  For example,

>>> romanize('Γιώργος Σχίζας')
Giorgos Schizas

You can call it as a module to translate the rest of the command line

>>> python -m romanize.py Γιώργος
'Giorgos'
"""


def romanize(greek_text):
    """Return the ISO 843:1997 transcription of the input Greek text.
    Any non-Greek characters will be ignored and printed as they were.newlett

    Examples:

    >>> romanize('Γιώργος Σχίζας')
    'Giorgos Schizas'
    >>> romanize('Θανάσης ΘΑΝΑΣΗΣ θΑνάσης ΘΑνάσης')
    'Thanasis THANASIS thAnasis THAnasis'
    >>> romanize('Αντώνης Ψαράς με ψάρια')
    'Antonis Psaras me psaria'
    >>> romanize('Αυγά αύριο παύση')
    'Avga avrio pafsi'
    >>> romanize('Άγγελος αρχάγγελος')
    'Angelos archangelos'
    >>> romanize('Ξάδελφος εξ αγχιστείας')
    'Xadelfos ex anchisteias'
    >>> romanize('Ακούμπα κάτω τα μπαούλα Γιακούμπ')
    'Akoumpa kato ta baoula Giakoub'
    >>> romanize('Ζεύξη Ρίου-Αντιρρίου')
    'Zefxi Riou-Antirriou'
    >>> romanize('μεταγραφή')
    'metagrafi'
    >>> romanize('Ούτε το αγγούρι ούτε η αγκινάρα γράφονται με γξ')
    'Oute to angouri oute i agkinara grafontai me nx'
    >>> romanize('ΟΥΡΑΝΟΣ Ουρανός ουρανός οϋρανός')
    'OURANOS Ouranos ouranos oyranos'
    >>> romanize('Έχω ελέγξει το 100% της μεθόδου')
    'Echo elenxei to 100% tis methodou'
    """
    result = ""
    cursor = 0
    while cursor < len(greek_text):
        lett = greek_text[cursor]
        prev_letter = greek_text[cursor - 1] if cursor > 0 else ""
        next_letter = greek_text[cursor + 1] if cursor < len(greek_text) - 1 else ""
        third_letter = greek_text[cursor + 2] if cursor < len(greek_text) - 2 else ""

        is_upper = (lett.upper() == lett)
        is_upper2 = (next_letter.upper() == next_letter)
        lett = lett.lower()
        prev_letter = prev_letter.lower()
        next_letter = next_letter.lower()
        third_letter = third_letter.lower()

        simple_translation_greek = 'άβδέζήιίϊΐκλνξόπρσςτυύϋΰφωώ'
        simple_translation_latin = 'avdeziiiiiklnxoprsstyyyyfoo'

        digraph_translation_greek = "θχψ"
        digraph_translation_latin = "thchps"

        digraph_ypsilon_greek = "αεη"
        digraph_ypsilon_latin = "aei"
        digraph_ypsilon_beta = "βγδζλμνραάεέηήιίϊΐοόυύϋΰωώ"
        digraph_ypsilon_phi = "θκξπστφχψ"

        if lett in simple_translation_greek:
            newlett = simple_translation_latin[simple_translation_greek.index(lett)]
        elif lett in digraph_translation_greek:
            diphthong_index = digraph_translation_greek.index(lett)
            newlett = digraph_translation_latin[diphthong_index * 2:diphthong_index * 2 + 2]
        elif lett in digraph_ypsilon_greek:
            newlett = digraph_ypsilon_latin[digraph_ypsilon_greek.index(lett)]
            if next_letter in ["υ", "ύ"]:
                if third_letter in digraph_ypsilon_beta:
                    newlett += "v"
                    cursor += 1
                elif third_letter in digraph_ypsilon_phi:
                    newlett += "f"
                    cursor += 1
        elif lett == "γ":
            if next_letter == "γ":
                newlett = "ng"
                cursor += 1
            elif next_letter == "ξ":
                newlett = "nx"
                cursor += 1
            elif next_letter in "χ":
                newlett = "nch"
                cursor += 1
            else:
                newlett = "g"
        elif lett == "μ":
            if next_letter == "π":
                if prev_letter.strip() == "" or third_letter.strip() == "":
                    newlett = "b"
                    cursor += 1
                else:
                    newlett = "mp"
                    cursor += 1
            else:
                newlett = "m"
        elif lett == "ο":
            newlett = "o"
            if next_letter in ["υ", "ύ"]:
                newlett += "u"
                cursor += 1
        else:
            newlett = lett
        if is_upper:
            newlett = newlett[0].upper() + \
                      (newlett[1:].upper() if is_upper2 else newlett[1:].lower())
        result += newlett
        cursor += 1
    return result


def main():
    import sys

    if len(sys.argv) > 1:
        print(romanize(' '.join(sys.argv[1:])))
    else:
        words = sys.stdin.read()
        print(romanize(words))


if __name__ == "__main__":
    main()
