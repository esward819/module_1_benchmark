from django.test import SimpleTestCase
from django.http import response

class Warmup_1(SimpleTestCase):
    def test_candy(self):
        response = self.client.get("/warmup-1/not_string/candy")
        self.assertContains(response, 'not candy')
    def test_x(self):
        response = self.client.get("/warmup-1/not_string/x")
        self.assertContains(response, 'not x')
    def test_not_bad(self):
        response = self.client.get("/warmup-1/not_string/not bad")
        self.assertContains(response, 'not bad')



class String_1(SimpleTestCase):
    def test_Hi_Bye(self):
        response = self.client.get("/string-1/make_abba/Hi/Bye")
        self.assertContains(response, 'HiByeByeHi')
    def test_Yo_Alice(self):
        response = self.client.get("/string-1/make_abba/Yo/Alice")
        self.assertContains(response, 'YoAliceAliceYo')
    def test_What_Up(self):
        response = self.client.get("/string-1/make_abba/What/Up")
        self.assertContains(response, 'WhatUpUpWhat')

class Logic_2(SimpleTestCase):
    def test_1_2_10(self):
        response = self.client.get("/logic-2/close_far/1/2/10")
        self.assertContains(response, True)
    def test_1_2_3(self):
        response = self.client.get("/logic-2/close_far/1/2/3")
        self.assertContains(response, False)
    def test_4_1_3(self):
        response = self.client.get("/logic-2/close_far/4/1/3")
        self.assertContains(response, True)
