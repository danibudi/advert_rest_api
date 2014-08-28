import unittest
import django
#~ import urllib2
django.setup()
from django.test.client import Client
from django.test import TestCase
from distributor.models import Distributor, Advertisement, make_dist_adv_list
from django.core.files import File


class TestDistributorImpls(TestCase):

    def response(self, c, url):
        response = c.post(url, {'count': 1})
        keys = ["distributor", "banner", "banner_link"]
        for k in keys:
            self.assertIn(k, response.serialize())

    def test_distributors(self):
        distr_list = [('Apple', 10), ('Mozilla', 30), ('Linux', 60)]
        for distr_name, percent in distr_list:
            dist, created = Distributor.objects.get_or_create(
                name=distr_name, show_percent=percent)
            self.assertEquals(created, True)
            self.assertEquals(distr_name,
                              Distributor.objects.get(name=distr_name).name)
        distributors = Distributor.objects.all()
        self.assertTrue(len(distributors) >= 3)
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
                #~ for real testing we can read data from url -
                #~ it's timeconsuming, internet depended
                #~ baner_content = urllib2.urlopen(img_url).read()
                file_name = "./test_static_immages/" + img_list_static[distr][i]
                banner_static = open(file_name, "r")
                baner_content = banner_static.read()
                banner_static.close()
                banner = File(baner_content)
                distributor = Distributor.objects.get(name=distr_list[distr][0])
                a, c = Advertisement.objects.get_or_create(
                    distributor=distributor, banner=banner, banner_link=img_url)
                self.assertEquals(c, True)
        images_count = sum(len(x) for x in img_list)
        self.assertTrue(len(Advertisement.objects.all()) >= images_count)
        dist_adv_list = make_dist_adv_list()
        distributors = Distributor.objects.all()
        distr_percent_advs_list = []
        for dist in distributors:
            adverts_distr_list = [adv.id for adv in dist.advertisement_set.all()]
            distr_percent_advs_list.append((dist.name,
                                            dist.show_percent,
                                            adverts_distr_list))
        for target in distr_percent_advs_list:
            self.assertIn(target, dist_adv_list)
        self.assertTrue(len(target) <= len(dist_adv_list))

    def test_api(self):
        c = Client()
        self.response(c, '/advert')

    def test_api_pid(self):
        c = Client()
        self.response(c, '/pid')


if __name__ == '__main__':
    unittest.main()
