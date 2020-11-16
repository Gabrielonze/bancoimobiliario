from django.test import SimpleTestCase
from bancoimob.gameCore.models.Player import Player
from bancoimob.gameCore.models.Property import Property

class TestCase(SimpleTestCase):

    def test_diceInRange(self):
        p = Player('impulsive')
        self.assertIn(p.rollTheDice(), [1, 2, 3, 4, 5, 6])
    
    def test_rentIsLower(self):
        p = Property()
        self.assertTrue(p.price > p.rent)

    def test_isBuyable(self):
        p = Property()
        p.buy({"name": 'Old Owner'})
        p.buy({"name": 'Newer Owner'})
        self.assertTrue(p.owner["name"] == 'Old Owner')
