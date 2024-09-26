from django.db import models


class Book(models.Model):
    genre_choice = (
        ('Фантастика', "Фантастика"),
        ("Роман", "Роман"),
        ("Триллер", "Триллер"),
        ("Детектив", "Детектив"),
    )
    title = models.CharField(max_length=250,
                             verbose_name='Введите название книг',db_index=True, null=True)
    image = models.ImageField(upload_to='books/',
                              verbose_name='Загружите фото книги',db_index=True, null=True)
    description = models.TextField(verbose_name='Введите информацию коротко о книге',db_index=True, null=True)
    url_book = models.URLField(verbose_name='Введите ссылку на сайт с полным информацией о книге',db_index=True, null=True)
    price = models.IntegerField(verbose_name='Введите цену на книгу',db_index=True, null=True)
    email = models.EmailField(verbose_name='Введите Имейл для адресс книги',db_index=True, null=True)
    genre = models.CharField(choices=genre_choice, max_length=120, verbose_name='Выберите жанр книги', null=True, db_index=True)
    discount = models.IntegerField(verbose_name='Введите сумму скидки', null=True, db_index=True)
    author_the_book = models.CharField(max_length=100, verbose_name='Введите имя автора книги', null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

class ReviewBook(models.Model):
    book_review = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews', db_index=True )
    text_review = models.TextField(db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    def __str__(self):
        return f'{self.text_review} - {self.created_at}'