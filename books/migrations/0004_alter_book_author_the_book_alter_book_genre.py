# Generated by Django 5.1.1 on 2024-09-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_author_the_book_book_discount_alter_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_the_book',
            field=models.CharField(max_length=100, null=True, verbose_name='Введите имя автора книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Фантастика', 'Фантастика'), ('Роман', 'Роман'), ('Триллер', 'Триллер'), ('Детектив', 'Детектив')], max_length=120, null=True, verbose_name='Выберите жанр книги'),
        ),
    ]
