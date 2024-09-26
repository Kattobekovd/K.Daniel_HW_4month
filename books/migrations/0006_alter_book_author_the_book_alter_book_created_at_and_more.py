# Generated by Django 5.1.1 on 2024-09-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_reviewbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_the_book',
            field=models.CharField(db_index=True, max_length=100, null=True, verbose_name='Введите имя автора книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(db_index=True, null=True, verbose_name='Введите информацию коротко о книге'),
        ),
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Введите сумму скидки'),
        ),
        migrations.AlterField(
            model_name='book',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, null=True, verbose_name='Введите Имейл для адресс книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Фантастика', 'Фантастика'), ('Роман', 'Роман'), ('Триллер', 'Триллер'), ('Детектив', 'Детектив')], db_index=True, max_length=120, null=True, verbose_name='Выберите жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(db_index=True, null=True, upload_to='books/', verbose_name='Загружите фото книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(db_index=True, null=True, verbose_name='Введите цену на книгу'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, max_length=250, null=True, verbose_name='Введите название книг'),
        ),
        migrations.AlterField(
            model_name='book',
            name='url_book',
            field=models.URLField(db_index=True, null=True, verbose_name='Введите ссылку на сайт с полным информацией о книге'),
        ),
    ]
