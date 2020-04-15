import unittest
from kartony import ToPack


class TestPacking(unittest.TestCase):
    """
    Tests for packing method

    """

    def setUp(self):
        # setup class
        self.app = ToPack()


    def test_0_or_101(self):
        ''' test about class range'''
        with self.assertRaises(NameError):
            self.app.packing(0)
        with self.assertRaises(NameError):
            self.app.packing(101)
    
    def test(self):
        ''' test algorithm with client table'''
        tab= dict()
        tab[1] ={'maly': 1, 'sredni': 0, 'duzy': 0, 'zbiorczy':0}
        tab[2] ={'maly': 1, 'sredni': 0, 'duzy': 0, 'zbiorczy':0}
        tab[3] ={'maly': 1, 'sredni': 0, 'duzy': 0, 'zbiorczy':0}
        tab[4] ={'maly': 0, 'sredni': 1, 'duzy': 0, 'zbiorczy':0}
        tab[5] ={'maly': 0, 'sredni': 1, 'duzy': 0, 'zbiorczy':0}
        tab[6] ={'maly': 0, 'sredni': 1, 'duzy': 0, 'zbiorczy':0}
        tab[7] ={'maly': 0, 'sredni': 0, 'duzy': 1, 'zbiorczy':0}
        tab[8] ={'maly': 0, 'sredni': 0, 'duzy': 1, 'zbiorczy':0}
        tab[9] ={'maly': 0, 'sredni': 0, 'duzy': 1, 'zbiorczy':0}
        tab[10] ={'maly': 0, 'sredni': 2, 'duzy': 0, 'zbiorczy':1}
        tab[11] ={'maly': 0, 'sredni': 2, 'duzy': 0, 'zbiorczy':1}
        tab[12] ={'maly': 0, 'sredni': 2, 'duzy': 0, 'zbiorczy':1}
        tab[13] ={'maly': 0, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[14] ={'maly': 0, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[15] ={'maly': 0, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[16] ={'maly': 0, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[17] ={'maly': 0, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[18] ={'maly': 0, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[19] ={'maly': 1, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[20] ={'maly': 1, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[21] ={'maly': 1, 'sredni': 0, 'duzy': 2, 'zbiorczy':1}
        tab[22] ={'maly': 0, 'sredni': 1, 'duzy': 2, 'zbiorczy':1}
        tab[23] ={'maly': 0, 'sredni': 1, 'duzy': 2, 'zbiorczy':1}
        tab[24] ={'maly': 0, 'sredni': 1, 'duzy': 2, 'zbiorczy':1}
        tab[25] ={'maly': 0, 'sredni': 0, 'duzy': 3, 'zbiorczy':1}
        tab[26] ={'maly': 0, 'sredni': 0, 'duzy': 3, 'zbiorczy':1}
        tab[27] ={'maly': 0, 'sredni': 0, 'duzy': 3, 'zbiorczy':1}
        tab[28] ={'maly': 1, 'sredni': 0, 'duzy': 3, 'zbiorczy':2}
        tab[29] ={'maly': 1, 'sredni': 0, 'duzy': 3, 'zbiorczy':2}
        tab[30] ={'maly': 1, 'sredni': 0, 'duzy': 3, 'zbiorczy':2}
        tab[31] ={'maly': 0, 'sredni': 1, 'duzy': 3, 'zbiorczy':2}
        tab[32] ={'maly': 0, 'sredni': 1, 'duzy': 3, 'zbiorczy':2}
        tab[33] ={'maly': 0, 'sredni': 1, 'duzy': 3, 'zbiorczy':2}
        tab[34] ={'maly': 0, 'sredni': 0, 'duzy': 4, 'zbiorczy':2}
        tab[35] ={'maly': 0, 'sredni': 0, 'duzy': 4, 'zbiorczy':2}
        tab[36] ={'maly': 0, 'sredni': 0, 'duzy': 4, 'zbiorczy':2}
        for i in tab:
            x = self.app.packing(i)
            self.assertEqual(x.maly, tab[i]['maly'])
            self.assertEqual(x.sredni, tab[i]['sredni'])
            self.assertEqual(x.duzy, tab[i]['duzy'])


if __name__ == '__main__':
    unittest.main()

