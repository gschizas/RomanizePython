# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import subprocess
import sys
import unittest
from romanize import romanize
import colorama
from hexdump import hexdump


class TestCore(unittest.TestCase):
    def test_common_words(self):
        self.assertEqual(romanize(u'Γιώργος Σχίζας'), u'Giorgos Schizas')
        self.assertEqual(romanize(u'Θανάσης ΘΑΝΑΣΗΣ θΑνάσης ΘΑνάσης'), u'Thanasis THANASIS thAnasis THAnasis')
        self.assertEqual(romanize(u'Αντώνης Ψαράς με ψάρια'), u'Antonis Psaras me psaria')
        self.assertEqual(romanize(u'Αυγά αύριο παύση'), u'Avga avrio pafsi')
        self.assertEqual(romanize(u'Άγγελος αρχάγγελος'), u'Angelos archangelos')
        self.assertEqual(romanize(u'Ξάδελφος εξ αγχιστείας'), u'Xadelfos ex anchisteias')
        self.assertEqual(romanize(u'Ακούμπα κάτω τα μπαούλα Γιακούμπ'), u'Akoumpa kato ta baoula Giakoub')
        self.assertEqual(romanize(u'Ζεύξη Ρίου-Αντιρρίου'), u'Zefxi Riou-Antirriou')
        self.assertEqual(romanize(u'μεταγραφή'), u'metagrafi')
        self.assertEqual(romanize(u'Ούτε το αγγούρι ούτε η αγκινάρα γράφονται με γξ'),
                         u'Oute to angouri oute i agkinara grafontai me nx')
        self.assertEqual(romanize(u'ΟΥΡΑΝΟΣ Ουρανός ουρανός οϋρανός'), u'OURANOS Ouranos ouranos oyranos')
        self.assertEqual(romanize(u'Έχω ελέγξει το 100% της μεθόδου'), u'Echo elenxei to 100% tis methodou')
        self.assertEqual(romanize(u'Εύζωνοι'), u'Evzonoi')


class TestShell(unittest.TestCase):
    def test_pipe(self):
        colorama.init(autoreset=True)
        test_text = u"Γιώργος Σχίζας"
        # print(sys.executable)
        # cmd_line = u'"' + sys.executable + '" romanize'
        #print('>>>',cmd_line)
        p = subprocess.Popen([sys.executable, '-m', 'romanize'],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             cwd=os.getcwd())

        print(p.args)
        print(vars(p))
        result = p.communicate(test_text.encode())
        print()
        for result_line in result:
            hexdump(result_line)
        print()
        #error_data = p.stderr.read()
        #print(colorama.Fore.RED, error_data, sep='')
        #print(colorama.Fore.YELLOW, result.decode('cp737', errors='replace'), sep='')
        self.assertEqual(u'Giorgos Schizas', result)
