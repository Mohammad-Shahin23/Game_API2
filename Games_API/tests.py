from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Game


# Create your tests here.

class GameTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_Game = Game.objects.create(name='flower', owner=testuser1, desc="test desc ...")
        test_Game.save()

    def thigs_model(self):
        Game = Game.objects.get(id=1)
        actual_owner= str(Game.owner)
        actual_name = str(Game.name)
        actual_desc = str(Game.desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"flower")
        self.assertEqual(actual_desc,"test desc ...")
