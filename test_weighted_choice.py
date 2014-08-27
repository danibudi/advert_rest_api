import unittest
import random
import collections
from weighted_choice import advert_choice, advert_choice_pid, weighted_choice


class Random(unittest.TestCase):

    def setUp(self):
        random.seed(55)

    def test_advert_choice(self):
        distr_percent_advs_list = [('b', 10, [2, 4, 6, 7]),
                                   ('a', 70, [1, 5, 8]),
                                   ('c', 20, [9, 10, 11, 12])]
        advert_choisen = []
        stat = collections.defaultdict(int)
        for i in range(0, 1000):
            aa = advert_choice(distr_percent_advs_list)
            advert_choisen.append(aa)
            stat[aa[0]] += 1
        self.assertEquals({'a': 711, 'c': 185, 'b': 104}, stat)

    def test_advert_empty_one(self):
        distr_percent_advs_list = [('b', 10, []),
                                   ('a', 70, [1, 5, 8]),
                                   ('c', 20, [9, 10, 11, 12])]
        stat = collections.defaultdict(int)
        for i in range(0, 1000):
            aa = advert_choice(distr_percent_advs_list)
            stat[aa[0]] += 1
        self.assertEquals({'a': 784, 'c': 216}, stat)

    def test_advert_none(self):
        distr_percent_advs_list = [('b', 10, []),
                                   ('a', 70, []),
                                   ('c', 20, [])]
        self.assertRaises(ValueError, advert_choice, distr_percent_advs_list)
        self.assertRaises(ValueError, advert_choice, [])


class Pid(unittest.TestCase):

    def test_advert_pid(self):
        distr_percent_advs_list = [('b', 10, [2, 4, 6, 7]),
                                   ('a', 70, [1, 5, 8]),
                                   ('c', 20, [9, 10, 11, 12])]
        persistent = {}
        stat = collections.defaultdict(int)
        for i in range(0, 1000):
            aa = advert_choice_pid(distr_percent_advs_list, persistent)
            stat[aa[0]] += 1
        self.assertEquals({'a': 700, 'c': 200, 'b': 100}, dict(stat))

    def test_advert_pid_one_empty(self):
        distr_percent_advs_list = [('b', 10, [1, 5, 8]),
                                   ('a', 70, []),
                                   ('c', 20, [9, 10, 11, 12])]
        persistent = {}
        stat = collections.defaultdict(int)
        for i in range(0, 1000):
            aa = advert_choice_pid(distr_percent_advs_list, persistent)
            stat[aa[0]] += 1
        self.assertEquals({'b': 333, 'c': 667}, dict(stat))

    def test_advert_pid_none(self):
        distr_percent_advs_list = [('b', 10, []),
                                   ('a', 70, []),
                                   ('c', 20, [])]
        self.assertRaises(ValueError, advert_choice_pid,
                          distr_percent_advs_list, {})
        self.assertRaises(ValueError, advert_choice_pid, [], {})


if __name__ == '__main__':
    unittest.main()
