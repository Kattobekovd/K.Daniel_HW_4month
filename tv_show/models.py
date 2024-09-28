from django.db import models
from django.db.models import ImageField


class Movie(models.Model):
    genre_choice = (
        ('Фантастика', "Фантастика"),
        ("Роман", "Роман"),
        ("Триллер", "Триллер"),
        ("Детектив", "Детектив"),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=100, choices=genre_choice)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title