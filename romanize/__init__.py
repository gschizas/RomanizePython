# -*- coding: utf-8 -*-
__author__ = 'George Schizas'
__version__ = '1.0.2'

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
    Any non-Greek characters will be ignored and printed as they were."""

    result = ""
    cursor = 0
    while cursor < len(greek_text):
        letter = greek_text[cursor]
        prev_letter = greek_text[cursor - 1] if cursor > 0 else ""
        next_letter = greek_text[cursor + 1] if cursor < len(greek_text) - 1 else ""
        third_letter = greek_text[cursor + 2] if cursor < len(greek_text) - 2 else ""

        is_upper = (letter.upper() == letter)
        is_upper_next = (next_letter.upper() == next_letter)
        letter = letter.lower()
        prev_letter = prev_letter.lower()
        next_letter = next_letter.lower()
        third_letter = third_letter.lower()

        simple_translation_greek = u'άβδέζήιίϊΐκλνξόπρσςτυύϋΰφωώ'
        simple_translation_latin = u'avdeziiiiiklnxoprsstyyyyfoo'

        digraph_translation_greek = u'θχψ'
        digraph_translation_latin = u'thchps'

        digraph_ypsilon_greek = u'αεη'
        digraph_ypsilon_latin = u'aei'
        digraph_ypsilon_beta = u'βγδζλμνραάεέηήιίϊΐοόυύϋΰωώ'
        digraph_ypsilon_phi = u'θκξπστφχψ'

        if letter in simple_translation_greek:
            new_letter = simple_translation_latin[simple_translation_greek.index(letter)]
        elif letter in digraph_translation_greek:
            diphthong_index = digraph_translation_greek.index(letter)
            new_letter = digraph_translation_latin[diphthong_index * 2:diphthong_index * 2 + 2]
        elif letter in digraph_ypsilon_greek:
            new_letter = digraph_ypsilon_latin[digraph_ypsilon_greek.index(letter)]
            if next_letter in [u'υ', u'ύ']:
                if third_letter in digraph_ypsilon_beta:
                    new_letter += u'v'
                    cursor += 1
                elif third_letter in digraph_ypsilon_phi:
                    new_letter += u'f'
                    cursor += 1
        elif letter == u'γ':
            if next_letter == u'γ':
                new_letter = u'ng'
                cursor += 1
            elif next_letter == u'ξ':
                new_letter = u'nx'
                cursor += 1
            elif next_letter in u'χ':
                new_letter = u'nch'
                cursor += 1
            else:
                new_letter = u'g'
        elif letter == u'μ':
            if next_letter == u'π':
                if prev_letter.strip() == "" or third_letter.strip() == "":
                    new_letter = u'b'
                    cursor += 1
                else:
                    new_letter = u'mp'
                    cursor += 1
            else:
                new_letter = u'm'
        elif letter == u'ο':
            new_letter = u'o'
            if next_letter in [u'υ', u'ύ']:
                new_letter += u'u'
                cursor += 1
        else:
            new_letter = letter
        if is_upper:
            new_letter = new_letter[0].upper() + (new_letter[1:].upper() if is_upper_next else new_letter[1:].lower())
        result += new_letter
        cursor += 1
    return result


def cli():
    import sys
    if len(sys.argv) > 1:
        print(romanize(' '.join(sys.argv[1:])))
    else:
        for line in sys.stdin:
            if type(line) is bytes:
                line = line.decode(sys.stdin.encoding)
            print(romanize(line))
