import unittest
import django
django.setup()
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

#~ django.testcase
from django.test.client import Client
from django.test import TestCase
from distributor.models import Distributor, Advertisement


def userLogin(name='lennon@thebeatles.com', email='lennon@thebeatles.com',
              passw='johnpass'):
    try:
        User.objects.get(email=email)
    except:
        User.objects.create_user(name, email, passw)
    c = Client()
    assert c.login(username=name, password=passw)
    return c


class TestUsersImpls(TestCase):
    #~ def setUp(self):
        #~ self.c = userLogin()
        #~ self.user_john = User.objects.get(email='lennon@thebeatles.com')

    def test_distributors(self):
        #~ users = User.objects.all()
        #~ print (users)
        #~ self.c = Client()
        #~ ringo_pass = 'ringo@thebeatles.com'
        #~ user_ringo, created = User.objects.get_or_create(email=ringo_pass)
        distr_name ='Nivea'
        dist, created = Distributor.objects.get_or_create(name=distr_name, show_percent=60)
        distr_name ='Dove'
        dist, created = Distributor.objects.get_or_create(name=distr_name, show_percent=30)
        distributors = Distributor.objects.all()
        self.assertEquals(distr_name, Distributor.objects.get(name=distr_name).name)
        self.assertTrue(len(distributors) >= 2)


if __name__ == '__main__':
    unittest.main()
