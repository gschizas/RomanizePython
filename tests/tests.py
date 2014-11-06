# -*- coding: utf-8 -*-

import os
import sys
import unittest
from romanize import romanize


class TestCommonWords(unittest.TestCase):
    def test_inline(self):
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
