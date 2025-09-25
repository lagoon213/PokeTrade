from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    set_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    rarity = models.CharField(
        max_length=50,
        choices=[
            ('common', 'Common'),
            ('uncommon', 'Uncommon'),
            ('rare', 'Rare'),
            ('double rare', 'Double Rare'),
            ('ace spec rare', 'Ace Spec Rare'),
            ('illustration rare', 'Illustration Rare'),
            ('ultra rare', 'Ultra Rare'),
            ('special illustration rare', 'Special Illustration Rare'),
            ('hyper rare', 'Hyper Rare'),
            ('shiny rare', 'Shiny Rare'),
            ('shiny ultra rare', 'Shiny Ultra Rare'),
            ('black star promo', 'Black Star Promo')]),
    image_url = models.URLField()

    def __str__(self):
        return self.name
