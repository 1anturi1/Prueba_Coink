from django.test import TestCase
from .models import User

# Create your tests here.


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(
            name='Andres', email='prueba@gmail.com', city='Bogota')

    def test_name(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.name, 'Andres')

    def test_email(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.email, 'prueba@gmail.com')
        
    def test_city(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.city, 'Bogota')

    def test_not_name(self):
        user = User.objects.get(id=1)
        self.assertNotEquals(user.name, 'Andrea')

    def test_not_email(self):
        user = User.objects.get(id=1)
        self.assertNotEquals(user.email, 'prueba1@gmail.com')

    def test_not_city(self):
        user = User.objects.get(id=1)
        self.assertNotEquals(user.city, 'Zipaquira')
