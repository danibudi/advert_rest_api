import unittest
import os
import random
from django.test.client import Client
from django.test import TestCase
from distributor.models import Distributor, Advertisement, make_dist_adv_list
from django.core.files import File

BASE = os.path.dirname(__file__)


class TestDistributorImpls(TestCase):
    def setUp(self):
        distr_list = [('Apple', 10), ('Mozilla', 30), ('Linux', 60)]
        for distr_name, percent in distr_list:
            dist, created = Distributor.objects.get_or_create(
                name=distr_name, show_percent=percent)
            self.assertEquals(created, True)

        img_list = [
            ['http://findicons.com/icon/44228/blue_flower?id=44243',
             'http://images.my-addr.com/img/exam_gif_to_png_q1.png',
             'http://findicons.com/icon/130907/paper_flower?id=130922'],
            ['http://png-2.findicons.com/files/icons/168/yoga/128/butterfly_orange.png',
             'http://png-2.findicons.com/files/icons/168/yoga/128/butterfly_blue.png',
             'http://png-2.findicons.com/files/icons/168/yoga/128/butterfly_orange.png'],
            ['http://findicons.com/icon/44238/pink_flower?id=44261',
             'http://findicons.com/icon/44400/pollen_flower?id=44424',
             'http://findicons.com/icon/44229/red_flower?id=44246']]
        #~ to avoid internet connection and Mock - read static files
        img_list_static = [
            ['tux.jpeg', 'moz.jpeg', 'apple.jpeg'],
            ['b1.jpeg', 'red_flower.png', 'icq.png'],
            ['flowers.png', 'mac_blue_flowers.png', 'mac_orange_flowers.png']]
        for distr, immage in list(enumerate(img_list)):
            for i in range(0, len(immage)):
                img_url = immage[i]
                file_name = os.path.join(BASE,
                                         "test_static_immages",
                                         img_list_static[distr][i])
                distributor = Distributor.objects.get(name=distr_list[distr][0])
                with open(file_name, "r") as banner_static:
                    a = Advertisement.objects.create(
                        distributor=distributor,
                        banner_link=img_url,
                        banner=File(banner_static, file_name))
                    a.save()

    def response(self, c, url):
        c.post(url, {'count': 1})

    def test_distributors(self):
        self.assertEqual(len(Advertisement.objects.all()), 9)
        dist_adv_list = make_dist_adv_list()
        distr_percent_advs_list = []
        distributors = Distributor.objects.all()

        for dist in distributors:
            adverts_distr_list = [adv.id for adv in dist.advertisement_set.all()]
            distr_percent_advs_list.append((dist.id, dist.show_percent, adverts_distr_list))
        for target in distr_percent_advs_list:
            self.assertIn(target, dist_adv_list)
        self.assertTrue(len(target) <= len(dist_adv_list))

    def test_api(self):
        random.seed(55)
        c = Client()
        for i in range(0, 100):
            self.response(c, '/advert/')
        distr_percent = {d.id: (d.shown_adverts, d.show_percent)
            for d in Distributor.objects.all()}
        self.assertEqual(distr_percent, {1: (10, 10), 2: (25, 30), 3: (65, 60)})

    def test_api_pid(self):
        c = Client()
        for i in range(0, 100):
            self.response(c, '/pid/')
        distr_percent = {d.id: (d.shown_adverts, d.show_percent)
            for d in Distributor.objects.all()}
        self.assertEqual(distr_percent, {1: (10, 10), 2: (30, 30), 3: (60, 60)})


if __name__ == '__main__':
    unittest.main()
