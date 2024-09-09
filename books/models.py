from django.db import models


class Book(models.Model):
    genre_choice = (
        ('Фантастика', "Фантастика"),
        ("Роман", "Роман"),
        ("Триллер", "Триллер"),
        ("Детектив", "Детектив"),
    )
    title = models.CharField(max_length=250,
                             verbose_name='Введите название книг',)
    image = models.ImageField(upload_to='books/',
                              verbose_name='Загружите фото книги')
    description = models.TextField(verbose_name='Введите информацию коротко о книге')
    url_book = models.URLField(verbose_name='Введите ссылку на сайт с полным информацией о книге')
    price = models.IntegerField(verbose_name='Введите цену на книгу')
    email = models.EmailField(verbose_name='Введите Имейл для адресс книги')
    genre = models.CharField(choices=genre_choice, max_length=120, verbose_name='Выберите жанр книги', null=True)
    discount = models.IntegerField(verbose_name='Введите сумму скидки', null=True)
    author_the_book = models.CharField(max_length=100, verbose_name='Введите имя автора книги', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
