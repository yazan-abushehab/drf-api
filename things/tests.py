from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Thing


# Create your tests here.

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='yazan', password='pass')
        testuser1.save()

        test_thing = Thing.objects.create(name='pin', owner=testuser1, desc="pin pin ...")
        test_thing.save()

    def thigs_model(self):
        thing = Thing.objects.get(id=1)
        actual_owner= str(thing.owner)
        actual_name = str(thing.name)
        actual_desc = str(thing.desc)
        self.assertEqual(actual_owner,"yazan")
        self.assertEqual(actual_name,"pin")
        self.assertEqual(actual_desc,"pin pin ...")